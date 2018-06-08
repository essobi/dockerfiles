FROM ubuntu:16.04  
  
ENV PATH /usr/local/bin:$PATH  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget -O /tmp/fly
https://github.com/concourse/concourse/releases/download/v3.5.0/fly_linux_amd64
&& \  
mv /tmp/fly /usr/local/bin/fly && \  
chmod +x /usr/local/bin/fly  

