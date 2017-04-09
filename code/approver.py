import boto3
import mechanize
import os
import sys
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
    approve_link(link)
