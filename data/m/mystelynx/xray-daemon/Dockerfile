FROM amazonlinux:2  
LABEL maintainer="uraura <t@urau.la>"  
  
ADD https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-
east-2/xray-daemon/aws-xray-daemon-2.x.rpm /tmp  
RUN yum install -y shadow-utils  
RUN rpm -ivh /tmp/aws-xray-daemon-2.x.rpm  
  
ENTRYPOINT ["/usr/bin/xray", "--bind=0.0.0.0:2000"]  

