FROM python:2.7  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN arch="$(dpkg --print-architecture)" \  
&& set -x \  
&& curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \  
&& curl -o /usr/local/bin/gosu.asc -fSL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# WARNING: BE SURE NOT TO USE THE WORD 'FLOWER' IN THE ENV VARS  
# E.G. VIA LINKING OR MAESTRO-NG: THEY HAVE A SPECIAL MEANING IN FLOWER.  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r flower && useradd -r -g flower flower  
  
RUN pip install redis==2.10.5  
RUN pip install flower==0.9.1  
  
COPY docker-entrypoint.sh /  
  
# Default port  
EXPOSE 5555  
# Variables with default that can be overruled by environment vars during
docker run.  
ENV REDIS_HOST redis  
ENV REDIS_PORT 6379  
ENV REDIS_DATABASE 0  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["flower", "--port=5555"]  

