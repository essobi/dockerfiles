FROM java:8  
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
&& apt-get -y install curl zip  
  
# Java  
ENV JAVA_FILE_VERSION 8u144  
ENV JAVA_DISTRIB_VERSION b01  
ENV JAVA_VERSION 1.8.0_144  
  
COPY jdk-${JAVA_FILE_VERSION}-linux-x64.tar.gz /  
  
# Install java  
# https://www.digitalocean.com/community/tutorials/how-to-manually-install-
oracle-java-on-a-debian-or-ubuntu-vps  
RUN mkdir -p /opt/jdk \  
&& tar -zxf jdk-${JAVA_FILE_VERSION}-linux-x64.tar.gz -C /opt/jdk \  
&& rm jdk-${JAVA_FILE_VERSION}-linux-x64.tar.gz \  
&& update-alternatives --install /usr/bin/java java
/opt/jdk/jdk${JAVA_VERSION}/bin/java 100 \  
&& update-alternatives --install /usr/bin/javac javac
/opt/jdk/jdk${JAVA_VERSION}/bin/javac 100 \  
&& export JAVA_HOME=/opt/jdk/jdk${JAVA_VERSION}/  
  
# Setup useful environment variables  
ENV MINECRAFT_MOD_HOME /minecraft  
ENV MINECRAFT_MOD_ZIP mod.zip  
  
# Create user  
RUN groupadd -r minecraft --gid=1000 \  
&& useradd -r -g minecraft --uid=1000 minecraft  
  
# Download and install spigot  
RUN curl -Lsk "http://addons-
origin.cursecdn.com/files/2480/4/Space%20Astronomy%202%20Server%20Files%20-%20v1.3.0.zip"
\--output ${MINECRAFT_MOD_ZIP}  
  
# Unzip  
RUN mkdir -p ${MINECRAFT_MOD_HOME}  
RUN chown -R minecraft: ${MINECRAFT_MOD_HOME} ${MINECRAFT_MOD_ZIP}  
  
COPY docker-entrypoint.sh /  
RUN chown minecraft: docker-entrypoint.sh \  
&& chmod 700 docker-entrypoint.sh  
  
EXPOSE 25565  
VOLUME ["/minecraft"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

