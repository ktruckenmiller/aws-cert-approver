import boto3
import mechanize
import os
import sys
from pprint import pprint
reload(sys)
sys.setdefaultencoding('utf8')

def get_s3_file_from_event(event):
    s3_client = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    s3_client.download_file(bucket, key, '/tmp/email_file')
    return '/tmp/email_file'

def parse_link_from_email_file(the_file):
    msg = open(the_file, 'r').readlines()
    for m in msg:
        if "https://certificates.amazon.com/approvals?code=" in m:
            return m.strip()

def parse_cert_id_from_email(the_file):
    msg = open(the_file, 'r').readlines()
    for m in msg:
        if "Certificate identifier: " in m:
            return m.split('r:')[1].strip()

def is_acm(cert_id, context):

    ACCOUNT_ID = context.invoked_function_arn.split(":")[4]
    REGION = context.invoked_function_arn.split(":")[3]
    acm = boto3.client('acm', region_name=REGION)
    try:
        cert_dict = acm.describe_certificate(
            CertificateArn='arn:aws:acm:{}:{}:certificate/{}'.format(REGION, ACCOUNT_ID, cert_id)
        )
        print cert_dict['Certificate']
        if cert_dict['Certificate']['Status'] == 'PENDING_VALIDATION':
            return True

    except Exception as e:
        print e
        return False



def approve_link(link):
    def select_form(form):
        return form.attrs.get('action', None) == '/approvals'

    br = mechanize.Browser()
    br.open(link)
    response = br.response()
    br.select_form(predicate=select_form)
    br.submit()

def lambda_handler(event, context):
    email_file = get_s3_file_from_event(event)
    link = parse_link_from_email_file(email_file)
    cert_id = parse_cert_id_from_email(email_file)

    if is_acm(cert_id, context):
        approve_link(link)
