FROM fulcrum/alpine  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
RUN apk update && apk upgrade && \  
wget "s3.amazonaws.com/aws-cli/awscli-bundle.zip" -O "awscli-bundle.zip" && \  
unzip awscli-bundle.zip && \  
apk add --update groff less pigz python tar && \  
rm /var/cache/apk/* && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm awscli-bundle.zip && \  
rm -rf awscli-bundle  
  
ADD bacon /usr/local/bin/bacon  
ADD assetcompactor /usr/local/bin/assetcompactor  
  
ENTRYPOINT ["/usr/local/bin/assetcompactor"]

