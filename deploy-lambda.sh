#!/bin/sh
rm -rf roles
ansible-galaxy install -p roles/ -r requirements.yml
ansible-playbook -i ansible_connection=localhost deploy.yml -vvv
