FROM mostaza/trenini-display-x64-dev:v1.0.0  
ENV DEBIAN_FRONTEND=noninteractive  
  
# volumes permissions fix  
RUN apt-get -y --no-install-recommends install \  
ca-certificates \  
curl  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN mkdir /src /build /scripts  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

