FROM ubuntu:14.04.4  
  
MAINTAINER gennady.trafimenkov@gmail.com  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& add-apt-repository ppa:yandex-load/main \  
&& apt-get update \  
&& apt-get install -y phantom phantom-ssl yandex-tank \  
&& apt-get install -y python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/bin/yandex-tank"]  

