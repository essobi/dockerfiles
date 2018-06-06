FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y libaio1 ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CONVOY_VERSION v0.5.0.2-rancher  
ADD
https://github.com/rancher/convoy/releases/download/${CONVOY_VERSION}/convoy.tar.gz
/tmp/  
RUN tar xvf /tmp/convoy.tar.gz -C /tmp/ \  
&& cp /tmp/convoy/convoy* /usr/local/bin/ \  
&& rm /tmp/convoy.tar.gz  
  
ADD convoy-ebs /usr/local/bin/  
RUN chmod a+x /usr/local/bin/convoy-ebs  
  

