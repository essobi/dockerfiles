FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
python-openstackclient \  
git \  
ruby \  
python3-pip \  
python3-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install python-gitlab  
  
RUN curl -L -o /usr/local/bin/mc https://dl.minio.io/client/mc/release/linux-
amd64/mc && \  
chmod a+x /usr/local/bin/mc  
  
WORKDIR /tmp  
ENTRYPOINT []  

