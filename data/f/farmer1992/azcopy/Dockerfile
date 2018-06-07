FROM microsoft/dotnet:latest  
MAINTAINER Boshi Lian <farmer1992@gmail.com>  
  
RUN mkdir /tmp/azcopy && \  
wget -O /tmp/azcopy/azcopy.tar.gz https://aka.ms/downloadazcopyprlinux && \  
tar -xf /tmp/azcopy/azcopy.tar.gz -C /tmp/azcopy && \  
/tmp/azcopy/install.sh  
  
RUN rm -rf /tmp/azcopy  
  
CMD ["/usr/bin/azcopy"]  

