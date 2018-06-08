FROM ubuntu:rolling  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q && apt-get install -qy --no-install-recommends \  
texlive-full \  
python-pygments gnuplot \  
make git curl \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
VOLUME ["/data"]  

