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
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r diamond && useradd -r -g diamond diamond  
  
# Install diamond  
RUN pip install diamond==4.0.195  
  
# Config it  
COPY diamond.conf /etc/diamond/  
RUN mkdir /var/log/diamond  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["diamond", "--foreground"]  

