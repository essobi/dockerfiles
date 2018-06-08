FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends wget  
RUN wget --no-check-certificate -O sloppy
https://files.sloppy.io/sloppy-`uname -s`-`uname -m` && \  
chmod +x sloppy  
  
CMD bash  
  

