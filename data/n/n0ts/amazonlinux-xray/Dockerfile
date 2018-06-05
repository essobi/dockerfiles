FROM n0ts/amazonlinux  
  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
RUN set -x \  
&& cd /opt \  
&& curl -o daemon.zip https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-
assets.us-east-2/xray-daemon/aws-xray-daemon-linux-2.x.zip \  
&& unzip daemon.zip && cp xray /usr/bin/xray  
  
ENTRYPOINT ["/usr/bin/xray", "-b", "0.0.0.0:2000"]  
EXPOSE 2000/udp  

