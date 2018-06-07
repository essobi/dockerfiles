FROM debian:stretch  
  
RUN apt-get update && apt-get install -y make m4 curl \  
&& rm -rf /tmp/* /var/tmp/* \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -fr /tmp/*.deb \  
&& rm -rf /usr/share/man/?? \  
&& rm -rf /usr/share/man/??_*  

