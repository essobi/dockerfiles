FROM ubuntu:17.10  
LABEL maintainer="Greg Hawkins <os@curvelogic.co.uk>"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
netbase \  
ca-certificates \  
curl \  
xz-utils \  
libz-dev \  
libgmp3-dev \  
libghc-bzlib-dev \  
git \  
unzip \  
software-properties-common \  
python3-dev \  
python3-pip  
  
ENV LANG=C.UTF-8  
RUN pip3 install pipenv  
  
RUN rm -rf /var/lib/apt/lists  
  
RUN curl -L
https://github.com/commercialhaskell/stack/releases/download/v1.7.1/stack-1.7.1-linux-x86_64.tar.gz
| tar zx -C /tmp  
RUN mv /tmp/stack-1.7.1-linux-x86_64/stack /usr/local/bin  
RUN stack setup  
  
ENTRYPOINT /bin/bash  

