FROM microsoft/aspnetcore-build:2.0  
  
ENV DEBIAN_FRONTEND="noninteractive"  
  
RUN apt-get update \  
&& \  
apt-get install -y \  
apt-transport-https \  
lsb-release \  
ca-certificates \  
openssl \  
ssl-cert \  
less \  
unzip \  
&& \  
apt-get autoremove -y --purge && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
echo "..."  

