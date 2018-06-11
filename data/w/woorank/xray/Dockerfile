FROM debian:stable-slim  
  
ADD https://s3.amazonaws.com/aws-xray-assets.us-east-1/xray-daemon/aws-xray-
daemon-linux-1.x.zip /tmp  
RUN apt-get update && apt-get install -y ca-certificates openssl unzip &&
unzip /tmp/aws-xray-daemon-linux-1.x.zip -d /usr/bin && apt-get remove -y
unzip && apt-get clean  
  
ENTRYPOINT ["xray"]  

