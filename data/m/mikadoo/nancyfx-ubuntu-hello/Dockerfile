FROM ubuntu:14.04  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y mono-complete  
  
ADD ./publish/ /publish  
  
EXPOSE 8123  
CMD ["mono", "/publish/HelloWorld.exe"]  

