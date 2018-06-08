FROM buildpack-deps:trusty-curl  
MAINTAINER Software Craftsmen GmbH und CoKG <office@software-craftsmen.at>  
  
  
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
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates  
  
# The go.cd package pulls in openjdk-7  
RUN apt-get update && \  
apt-get install -y openssh-client git && \  
echo "deb https://download.go.cd /" | sudo tee
/etc/apt/sources.list.d/gocd.list && \  
apt-get install -y apt-transport-https && \  
wget -O - https://download.go.cd/GOCD-GPG-KEY.asc | sudo apt-key add - && \  
apt-get update && \  
apt-get install -y go-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
sed -i -e 's/DAEMON=Y/DAEMON=N/' /etc/default/go-server  
  
ADD cruise-config.xml cruise-config.xml  
ADD docker-entrypoint.sh docker-entrypoint.sh  
  
ENV ARTIFACTS_LOCATION=/var/lib/go-server/artifacts  
  
RUN chmod +x docker-entrypoint.sh  
  
EXPOSE 8153 8154  
CMD ./docker-entrypoint.sh  

