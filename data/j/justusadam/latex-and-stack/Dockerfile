FROM buildpack-deps:xenial  
  
ENV STACK_DOWNLOAD_URL https://www.stackage.org/stack/linux-x86_64  
# ENV DEBIAN_FRONTEND noninteractive  
ENV PATH $PATH:/root/.local/bin  
ENV LANG C.UTF-8  
RUN apt-get update -q && \  
apt-get install -qy texlive-full libgmp-dev python python-dev python-pip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /root/.local/bin && \  
wget -q -O- $STACK_DOWNLOAD_URL | tar --strip=1 -xvz -C /root/.local/bin/ && \  
chmod +x /root/.local/bin/stack  
  
RUN pip install pygments  

