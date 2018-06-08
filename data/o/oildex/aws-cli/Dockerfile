FROM python:3.6.5-alpine3.7  
  
ENV AWSCLI_VERSION=1.15.4  
  
RUN pip install awscli==$AWSCLI_VERSION  
RUN apk add --no-cache --virtual .run-deps \  
groff \  
less  
  
CMD ["/usr/local/bin/aws", "--version"]  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="aws-cli" \  
org.label-schema.version="1.15.4" \  
org.label-schema.url="https://aws.amazon.com/cli/" \  
org.label-schema.vcs-url="https://github.com/oildex/docker-aws-cli"  

