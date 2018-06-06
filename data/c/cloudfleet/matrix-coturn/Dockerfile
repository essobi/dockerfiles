FROM debian:jessie  
  
# Maintainer  
MAINTAINER Silvio Fricke <silvio.fricke@gmail.com> \+ jon richter
<almereyda@allmende.io>  
  
# update and upgrade  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libevent-dev \  
libffi-dev \  
libjpeg-dev \  
libsqlite3-dev \  
libssl-dev \  
pwgen \  
python-pip \  
python-virtualenv \  
python2.7-dev \  
sqlite3 \  
unzip \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# install homerserver template  
ADD adds/start.sh /start.sh  
RUN chmod a+x /start.sh  
  
# startup configuration  
ENTRYPOINT ["/start.sh"]  
CMD ["start"]  
EXPOSE 3478  
VOLUME ["/data"]  
  
# install/upgrade pip  
RUN pip install --upgrade pip setuptools  
  
# "git clone" is cached, we need to invalidate the docker cache here  
# to use this add a --build-arg INVALIDATEBUILD=$(data) to your docker build  
# parameter.  
ENV INVALIDATEBUILD=notinvalidated  
  
# install turn-server  
ENV BV_TUR=master  
ADD https://github.com/coturn/coturn/archive/$BV_TUR.zip c.zip  
RUN unzip c.zip \  
&& rm c.zip \  
&& cd /coturn-$BV_TUR \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /coturn-$BV_TUR  

