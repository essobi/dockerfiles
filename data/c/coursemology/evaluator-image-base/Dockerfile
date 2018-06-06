FROM debian:8  
MAINTAINER Coursemology <coursemology@googlegroups.com>  
  
RUN apt-get update && apt-get install -y --force-yes \  
make \  
&& rm -rf /var/lib/apt/lists/*  
RUN groupadd -r coursemology \  
&& useradd -r -g coursemology -m coursemology  
  
# grab gosu for easy step-down from root  
# from official Postgres image; remove when gosu is added to Debian repository  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
COPY usr /usr  
ENTRYPOINT ["/usr/local/bin/coursemology-evaluate.sh"]  

