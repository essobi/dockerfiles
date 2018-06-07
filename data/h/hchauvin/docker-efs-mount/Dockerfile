FROM python:alpine  
RUN apk add --update nfs-utils bash curl zip jq && \  
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -rf awscli-bundle && \  
rm awscli-bundle.zip && \  
apk del curl zip && \  
rm -rf /var/cache/apk/*  
  
ADD ./entry.sh /entry.sh  
RUN chmod +x /entry.sh  
  
ENTRYPOINT ["/entry.sh" ]  

