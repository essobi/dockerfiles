FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
texlive-full \  
gnuplot \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/*  

