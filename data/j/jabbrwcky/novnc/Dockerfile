FROM ubuntu:16.04  
EXPOSE 6080  
RUN apt-get update && apt-get install -y \  
apt-utils \  
net-tools \  
git \  
python \  
python-numpy \  
python-pip\  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install python-memcached  
  
COPY . /app/  
WORKDIR /app  
  
RUN cd /app/utils \  
&& git clone \--depth 1 https://source.xing.com/jens-hausherr/websockify.git  
  
ENTRYPOINT [ "utils/launch.sh" ]  

