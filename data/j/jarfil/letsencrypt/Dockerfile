FROM debian:stretch  
  
MAINTAINER Jaroslaw Filiochowski <jarfil@gmail.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
letsencrypt \  
&& \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD letsencrypt  

