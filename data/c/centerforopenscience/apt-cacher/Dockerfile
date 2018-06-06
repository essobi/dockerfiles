FROM debian:jessie  
  
# Install dependancies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apt-cacher \  
apache2 \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.4  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get clean \  
&& apt-get autoremove -y \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3142  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [ "apt-cacher" ]

