FROM ubuntu:16.04  
MAINTAINER Paul Rohja Lesellier <rohja@rohja.com>  
  
ENV AWS_REGION us-west-1  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends
apt-transport-https curl ca-certificates wget && apt-get clean && apt-get
autoremove && rm -rf /var/lib/apt/lists/*  
RUN wget https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-
east-2/xray-daemon/aws-xray-daemon-2.x.deb  
RUN dpkg -i aws-xray-daemon-2.x.deb && rm aws-xray-daemon-2.x.deb  
CMD ["/usr/bin/xray", "--bind=0.0.0.0:2000"]  
EXPOSE 2000/udp  

