FROM ubuntu:16.04  
  
MAINTAINER Jonatan Allegrini <jallegri@gmail.com>  
  
RUN \  
apt-get update && \  
printf no\n | apt-get install -y jackd2 --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get update && \  
printf no\n | apt-get install -y jack --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get update && \  
apt-get install -y ubuntustudio-audio-plugins && \  
rm -rf /var/lib/apt/lists/*  

