#!/bin/sh
ansible-galaxy install -p roles/ -r requirements.yml

docker run -it --rm \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $(pwd):/code \
--entrypoint="" \
-e IAM_ROLE="cloudformation" \
ktruckenmiller/ansible:dind \
ansible-playbook -i ansible_connection=local deploy.yml -vvv
