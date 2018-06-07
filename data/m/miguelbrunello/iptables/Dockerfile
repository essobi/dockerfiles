# iptables  
#  
# VERSION 1.0  
FROM miguelbrunello/base  
MAINTAINER Miguel Brunello <miguel.brunello@unc.edu.ar>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y \  
iptables \  
nmap  
  
RUN apt-get update && apt-get install -y \  
linux-image-$(uname -r)  
  

