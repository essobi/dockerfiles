FROM igaguri/base-ubuntu-16.04  
# https://hub.docker.com/r/igaguri/base-ubuntu-16.04  
  
MAINTAINER iganari  
  
### install cmatrix  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y cmatrix  
  
  
### add asciiquarium  
RUN add-apt-repository -y ppa:ytvwld/asciiquarium && \  
apt-get update &&\  
apt-get install -y asciiquarium &&\  
cp $(find / -name "asciiquarium" | grep -v doc | grep -v menu) /usr/local/bin/
&&\  
chmod 755 /usr/local/bin/asciiquarium  

