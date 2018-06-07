###############################################  
# Teamspeak 3 Server on ubuntu.  
###############################################  
# Using latest Ubuntu image as base  
FROM ubuntu:trusty  
MAINTAINER Daniele Riccucci "daniele.riccucci@gmail.com"  
RUN groupadd -r ts3 && useradd -r -g ts3 ts3  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl \  
&& rm -r /var/lib/apt/lists/*  
  
ENV TEAMSPEAK_VERSION 3.0.11.4  
ENV TEAMSPEAK_SHA1 09e7fc2cb5dddf84f3356ddd555ad361f5854321  
ENV TEAMSPEAK_BASE_URL http://dl.4players.de/ts  
  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Download TS3 file and extract it into /opt.  
RUN mkdir -p /opt/teamspeak3-server  
RUN curl -o /tmp/teamspeak3-server_linux-amd64.tar.gz
${TEAMSPEAK_BASE_URL}/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux-
amd64-${TEAMSPEAK_VERSION}.tar.gz \  
&& echo "${TEAMSPEAK_SHA1} */tmp/teamspeak3-server_linux-amd64.tar.gz" |
sha1sum -c - \  
&& tar -C /opt/teamspeak3-server --strip-components=1 -xzf
/tmp/teamspeak3-server_linux-amd64.tar.gz \  
&& rm /tmp/teamspeak3-server_linux-amd64.tar.gz  
  
RUN cp /opt/teamspeak3-server/redist/libmariadb.so.2 /opt/teamspeak3-server/  
RUN chown -R ts3:ts3 /opt/teamspeak3-server  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME /ts3  
  
# Expose the Standard TS3 port.  
EXPOSE 9987/udp  
# for ServerQuery  
EXPOSE 10011  
# for files  
EXPOSE 30033  

