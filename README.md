# AWS ACM Auto approver

Dependencies:
- Docker
- https://github.com/ktruckenmiller/docker-friend

 to deploy ( docker-friend authenticated )

 `make`


*To auto approve a cert, make sure that you have SES making amazon spit that acm admin
email to the s3 bucket that this cloudformation creates.
