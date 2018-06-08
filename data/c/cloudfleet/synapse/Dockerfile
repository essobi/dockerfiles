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
python-ldap \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# install/upgrade pip  
RUN pip install --upgrade pip setuptools  
  
# "git clone" is cached, we need to invalidate the docker cache here  
# to use this add a --build-arg INVALIDATEBUILD=$(data) to your docker build  
# parameter.  
ENV INVALIDATEBUILD=notinvalidated  
  
# install synapse homeserver  
ENV BV_SYN=develop  
RUN curl -fSL https://github.com/matrix-org/synapse/archive/$BV_SYN.zip -o
s.zip \  
&& unzip s.zip \  
&& rm s.zip \  
&& cd /synapse-$BV_SYN \  
&& pip install --process-dependency-links . \  
&& echo $BV_SYN > /synapse.version \  
&& rm -rf /synapse-$BV_SYN  
  
# install homerserver template  
ADD adds/start.sh /start.sh  
RUN chmod a+x /start.sh  
  
# startup configuration  
ENTRYPOINT ["/start.sh"]  
CMD ["start"]  
EXPOSE 8448  
VOLUME ["/data"]  

