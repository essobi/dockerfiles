FROM iron/node:dev  
MAINTAINER Mateusz Pawlowski <mateusz@generik.co.uk>  
LABEL kind=cli-tool  
VOLUME /root  
WORKDIR /root  
  
ENV AZURE_CLI_VERSION 0.9.14  
RUN apk --update add python make g++ && \  
npm install --global azure-cli@$AZURE_CLI_VERSION && \  
apk del python make g++ ; rm -rf /var/cache/apk/* ; \  
apk stats ; \  
azure  

