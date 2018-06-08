FROM phusion/baseimage:0.10.0  
MAINTAINER rui@deniable.org  
  
LABEL description="Base image for manticore"  
  
ENV WRKSRC /opt  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install python-pip git build-essential && \  
cd $WRKSRC && \  
git clone https://github.com/trailofbits/manticore.git && \  
cd manticore && \  
pip install . && \  
useradd -m manticore && \  
echo manticore:manticore | chpasswd && usermod -aG sudo manticore && \  
cd $WRKSRC && chown -R manticore:manticore manticore && \  
rm -rf /var/lib/apt/lists/*  
  
USER manticore  
WORKDIR /home/manticore  
ENV HOME /home/manticore  
  
CMD ["/bin/bash"]  

