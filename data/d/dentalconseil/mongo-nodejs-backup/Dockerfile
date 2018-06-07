FROM node:4.4  
  
RUN mkdir -p /nodeapp /config /backup  
  
RUN cd /tmp && apt-get update && apt-get install unzip && \  
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -R *  
  
ENV S3_REGION="eu-west-1"  
  
WORKDIR /nodeapp  
  
COPY . .  
RUN npm install  
  
VOLUME /config  
VOLUME /backup  
  
RUN chmod a+x bootstrap.sh  
CMD ./bootstrap.sh  

