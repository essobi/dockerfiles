FROM n0ts/ubuntu  
  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
RUN set -x \  
&& wget https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-
east-2/xray-daemon/aws-xray-daemon-2.x.deb \  
&& dpkg -i aws-xray-daemon-2.x.deb  
  
CMD ["/usr/bin/xray", "--bind=0.0.0.0:2000"]  
EXPOSE 2000/udp  

