FROM java:7  
MAINTAINER John Paul Alcala, jpalcala@ayannah.com  
  
ENV ARCHIVA_VERSION 2.2.0  
# Taken from Postgres Official Dockerfile.  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN mkdir -p /opt/apache-archiva && \  
curl -SL http://apache.claz.org/archiva/$ARCHIVA_VERSION/binaries/apache-
archiva-$ARCHIVA_VERSION-bin.tar.gz | tar xzf - -C /opt/apache-archiva
--strip-components=1 && \  
useradd -rM archiva && \  
chown -R archiva:archiva /opt/apache-archiva/  
  
COPY entrypoint.sh /  
  
VOLUME ["/opt/apache-archiva/repositories", "/opt/apache-archiva/logs",
"/opt/apache-archiva/data"]  
  
EXPOSE 8080  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["archiva"]  

