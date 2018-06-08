FROM ubuntu:16.04  
# From https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-
ecs.html?icmpid=docs_xray_console  
# Install CA certificates  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends
apt-transport-https curl ca-certificates wget && apt-get clean && apt-get
autoremove && rm -rf /var/lib/apt/lists/*  
  
RUN wget https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-
east-2/xray-daemon/aws-xray-daemon-2.x.deb  
  
RUN dpkg -i aws-xray-daemon-2.x.deb  
  
EXPOSE 2000/udp  
# Run the X-Ray daemon  
ENTRYPOINT ["/usr/bin/xray", "--bind", "0.0.0.0:2000"]  
CMD [""]  

