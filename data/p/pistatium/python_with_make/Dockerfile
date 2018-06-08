FROM python:3.6  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN apt-get install -y make  
  
VOLUME /root  
WORKDIR /root  

