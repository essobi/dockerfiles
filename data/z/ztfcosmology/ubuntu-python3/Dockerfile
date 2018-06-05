  
FROM ubuntu:17.04  
MAINTAINER jvansanten  
  
RUN apt-get update \  
&& apt-get install -y python3-pip \  
&& apt-get clean \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& ln -s /usr/bin/pip3 pip \  
&& pip3 install \--upgrade pip  
  
RUN apt-get install -y python3-astropy python3-scipy ipython3 python3-shapely
\  
&& apt-get clean \  
&& ln -s /usr/bin/ipython3 /usr/local/bin/ipython  

