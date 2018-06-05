FROM alpine  
RUN apk update && apk add python py-pip && rm -rf /var/cache/apk/*  
RUN pip install awscli  
RUN pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-
bootstrap-latest.tar.gz  
  

