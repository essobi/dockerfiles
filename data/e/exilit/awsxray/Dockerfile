FROM debian:stable-slim  
  
ENV AWS_ACCESS_KEY_ID=  
ENV AWS_SECRET_ACCESS_KEY=  
ENV AWS_REGION=  
  
ADD https://s3.dualstack.eu-west-1.amazonaws.com/aws-xray-assets.eu-
west-1/xray-daemon/aws-xray-daemon-2.x.deb /tmp  
RUN cd /tmp/ && \  
apt-get update && \  
apt-get install -y ca-certificates && \  
dpkg -i aws-xray-daemon-2.x.deb && \  
rm aws-xray-daemon-2.x.deb  
  
EXPOSE 2000/udp  
  
ENTRYPOINT ["/usr/bin/xray", "--bind", "0.0.0.0:2000"]  
CMD [""]  

