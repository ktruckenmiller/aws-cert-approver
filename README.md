# AWS ACM Auto approver

Dependencies:
- Docker
- https://github.com/ktruckenmiller/docker-friend
- An AWS role that can deploy cloudformation SAM


First, make sure you're authenticate with docker-friend and MFA, and that the
Makefile has the proper IAM_ROLE for permissions to deploy cloudformation.

Then to deploy, simply type:

 `make`


*To auto approve a cert, make sure that you have SES making amazon spit that acm admin
email to the s3 bucket that this cloudformation creates.

![Diagram](https://cloudcraft.co/view/e0bdbc36-b737-4a48-adf4-24d484ef0740?key=p7vDw9bhwD7LLvZ_6VZxTg)


