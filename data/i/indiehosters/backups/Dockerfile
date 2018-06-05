FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV VERSION=0.7.09  
  
RUN apt-get update \  
&& apt-get install -y --force-yes apt-transport-https ca-certificates \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y \  
docker-engine=1.8.3-0~jessie \  
wget \  
python \  
python-dev \  
python-pip \  
libffi-dev \  
librsync-dev \  
libssl-dev \  
ncftp \  
lftp \  
rsync \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install --upgrade cffi lockfile paramiko pycrypto \  
&& cd /tmp/ \  
&& wget
https://launchpad.net/duplicity/0.7-series/$VERSION/+download/duplicity-$VERSION.tar.gz
\  
&& cd /opt/ \  
&& tar xzvf /tmp/duplicity-$VERSION.tar.gz \  
&& rm /tmp/duplicity-$VERSION.tar.gz \  
&& cd duplicity-$VERSION \  
&& ./setup.py install  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

