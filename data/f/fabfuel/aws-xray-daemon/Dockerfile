FROM amazonlinux  
  
RUN yum install -y wget unzip  
  
RUN wget https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-
east-2/xray-daemon/aws-xray-daemon-linux-2.x.zip && \  
unzip aws-xray-daemon-linux-2.x.zip && \  
mv xray /usr/bin/xray  
  
COPY cfg.yaml /usr/src/app/  
  
ENV AWS_ACCESS_KEY_ID ""  
ENV AWS_SECRET_ACCESS_KEY ""  
EXPOSE 20000/udp  
  
ENTRYPOINT ["/usr/bin/xray", "-c", "/usr/src/app/cfg.yaml"]  

