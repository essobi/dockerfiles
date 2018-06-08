FROM debian:latest  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
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
  
# Install curl  
RUN apt-get --quiet update \  
&& apt-get -y install curl  
  
# Install java  
ENV JAVA_FILE_VERSION 8u71  
ENV JAVA_DISTRIB_VERSION b15  
ENV JAVA_VERSION 1.8.0_71  
# https://www.digitalocean.com/community/tutorials/how-to-manually-install-
oracle-java-on-a-debian-or-ubuntu-vps  
RUN curl -#LO --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_FILE_VERSION}-${JAVA_DISTRIB_VERSION}/jdk-${JAVA_FILE_VERSION}-linux-x64.tar.gz
\  
&& mkdir -p /opt/jdk \  
&& tar -zxf jdk-${JAVA_FILE_VERSION}-linux-x64.tar.gz -C /opt/jdk \  
&& rm jdk-${JAVA_FILE_VERSION}-linux-x64.tar.gz \  
&& update-alternatives --install /usr/bin/java java
/opt/jdk/jdk${JAVA_VERSION}/bin/java 100 \  
&& update-alternatives --install /usr/bin/javac javac
/opt/jdk/jdk${JAVA_VERSION}/bin/javac 100 \  
&& export JAVA_HOME=/opt/jdk/jdk${JAVA_VERSION}/  
  
# Setup useful environment variables  
ENV SPIGOT_HOME /minecraft  
ENV SPIGOT_DATA /data  
ENV SPIGOT_BIN $SPIGOT_HOME/spigot.jar  
ENV SPIGOT_VERSION 1.11.2  
# Create user  
RUN groupadd -r minecraft --gid=1000 \  
&& useradd -r -g minecraft --uid=1000 minecraft  
  
# Create minecraft directories  
RUN mkdir -p "${SPIGOT_HOME}" \  
&& mkdir -p "${SPIGOT_DATA}" \  
&& chown -R minecraft: "${SPIGOT_HOME}" \  
&& chmod -R 700 "${SPIGOT_HOME}"  
  
# Download and install spigot  
RUN curl -Ls "https://cdn.getbukkit.org/spigot/spigot-${SPIGOT_VERSION}.jar"
\--output ${SPIGOT_BIN}  
  
# Setup permissions  
RUN chown -R minecraft: "${SPIGOT_HOME}" \  
&& chown -R minecraft: "${SPIGOT_DATA}"  
  
COPY docker-entrypoint.sh /  
RUN chown minecraft: docker-entrypoint.sh \  
&& chmod 700 docker-entrypoint.sh  
  
EXPOSE 25565  
VOLUME ["/data"]  
WORKDIR ${SPIGOT_DATA}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

