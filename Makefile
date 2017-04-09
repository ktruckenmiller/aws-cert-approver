current_dir=~/Projects/aws-cert-approver
deploy:
	docker run -it --rm \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v $(current_dir):/code \
	--entrypoint="" \
	-e IAM_ROLE="cloudformation" \
	ktruckenmiller/ansible:dind \
	./deploy-lambda.sh
