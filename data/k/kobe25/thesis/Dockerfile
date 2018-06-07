FROM debian:8  
  
MAINTAINER Antonio Esposito "kobe@befair.it"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update && \  
apt install -y texlive-full && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /code  

