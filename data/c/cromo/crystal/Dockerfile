FROM debian:wheezy  
MAINTAINER Cristian Romo "cristian.g.romo@gmail.com"  
RUN apt-get update && \  
apt-get install -y \  
curl \  
gcc && \  
rm -rf /var/lib/apt/lists/*  
RUN curl --location -o crystal-0.6.1-1-linux-x86_64.tar.gz
https://github.com/manastech/crystal/releases/download/0.6.1/crystal-0.6.1-1-linux-x86_64.tar.gz
&& \  
tar xzvf crystal-0.6.1-1-linux-x86_64.tar.gz && \  
rm crystal-0.6.1-1-linux-x86_64.tar.gz && \  
mv crystal-0.6.1-1 /opt/crystal && \  
ln -s /opt/crystal/bin/crystal /usr/local/bin/crystal  
  
WORKDIR /source  
CMD ["bash"]

