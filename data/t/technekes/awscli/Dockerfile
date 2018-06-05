FROM alpine:latest  
  
MAINTAINER John Allen <john.allen@technekes.com>  
  
RUN wget "s3.amazonaws.com/aws-cli/awscli-bundle.zip" -O "awscli-bundle.zip"
&& \  
unzip awscli-bundle.zip && \  
apk add --update groff less python && \  
rm /var/cache/apk/* && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm awscli-bundle.zip && \  
rm -rf awscli-bundle  
  
ENTRYPOINT ["aws"]  

