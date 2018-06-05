FROM debian:jessie  
  
MAINTAINER Ilya Epifanov <elijah.epifanov@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y curl ca-certificates --no-install-recommends \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
ENV AMC_VERSION=3.6.0  
RUN curl -o /tmp/aerospike-amc-community-${AMC_VERSION}.all.x86_64.deb -SL
"http://www.aerospike.com/download/amc/${AMC_VERSION}/artifact/debian6" \  
&& apt-get update \  
&& apt-get install -y python python-dev gcc --no-install-recommends \  
&& dpkg -i /tmp/aerospike-amc-community-${AMC_VERSION}.all.x86_64.deb \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME /var/log/amc  
  
EXPOSE 8081  
CMD ["/opt/amc/bin/gunicorn", "--config=/etc/amc/config/gunicorn_config.py",
"flaskapp:app"]  
  

