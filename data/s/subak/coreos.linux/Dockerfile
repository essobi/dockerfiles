FROM buildpack-deps:stretch  
  
RUN cd /usr/src \  
&& git clone \--progress https://github.com/coreos/linux.git  
  
RUN apt-get update && apt-get install -y bc  

