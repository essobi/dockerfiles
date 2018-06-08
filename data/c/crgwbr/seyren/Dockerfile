FROM java:openjdk-7-jre  
MAINTAINER Craig Weber "crgwbr@gmail.com"  
ENV SEYREN_VERSION 1.3.0  
ENV SEYREN_GROUP seyren  
ENV SEYREN_USER seyren  
ENV HOME /var/lib/seyren  
  
RUN groupadd -r $SEYREN_GROUP -g 433  
RUN useradd -u 431 -r -g $SEYREN_GROUP -d $HOME -s /sbin/nologin -c "Seyren
user" $SEYREN_USER  
  
RUN mkdir -p $HOME  
RUN chown -R $SEYREN_USER:$SEYREN_GROUP $HOME  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Fetch Seyren  
RUN wget
http://github.com/scobal/seyren/releases/download/"$SEYREN_VERSION"/seyren-"$SEYREN_VERSION".jar
-O $HOME/seyren.jar  
  
COPY run-seyren.sh /run-seyren.sh  
RUN chmod +x /run-seyren.sh  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8080  
CMD ["/run-seyren.sh"]  

