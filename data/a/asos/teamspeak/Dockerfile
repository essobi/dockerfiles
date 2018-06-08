FROM debian:jessie  
MAINTAINER Reesey275 <reesey275@gmail.com>  
  
ENV TS3_USER=teamspeak \  
TS3_GROUP=teamspeak \  
TS3_HOME=/teamspeak \  
TS3_FILES=/teamspeak/files \  
TS3_VERSION=3.1.3 \  
TS3_FILENAME=teamspeak3-server_linux_amd64  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="ASoS Teamspeak 3 Docker" \  
org.label-schema.description="A docker container for running a teamspeak
server with a MySQL/MariaDB Database." \  
org.label-schema.url="http://www.asosgaming.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/asosgaming/teamspeak" \  
org.label-schema.vendor="ASoS Gaming Community" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh && \  
apt-get -q update && \  
apt-get -q install -y \  
apt-utils \  
locales \  
wget \  
sudo \  
nano \  
mysql-common \  
libxcursor1 \  
libglib2.0-0 \  
libreadline5 \  
bzip2 \  
tar \  
sqlite3 \  
ca-certificates && \  
groupadd -g 4000 -r ${TS3_GROUP} && \  
useradd -u 4000 -r -m -g ${TS3_GROUP} -d ${TS3_HOME} ${TS3_USER} && \  
update-ca-certificates && \  
export TZ=America/New_York && \  
locale-gen --purge en_US.UTF-8 && \  
echo LC_ALL=en_US.UTF-8 >> /etc/default/locale && \  
echo LANG=en_US.UTF-8 >> /etc/default/locale && \  
apt-get -qq clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir -p ${TS3_FILES}  
  
WORKDIR ${TS3_HOME}  
  
RUN wget
"http://dl.4players.de/ts/releases/${TS3_VERSION}/${TS3_FILENAME}-${TS3_VERSION}.tar.bz2"
-O ${TS3_FILENAME}-${TS3_VERSION}.tar.bz2 \  
&& tar -xjf "${TS3_FILENAME}-${TS3_VERSION}.tar.bz2" \  
&& rm ${TS3_FILENAME}-${TS3_VERSION}.tar.bz2 \  
&& cp -r ${TS3_FILENAME}/* ${TS3_HOME} \  
&& rm -r ${TS3_HOME}/tsdns \  
&& rm -r ${TS3_FILENAME}  
  
RUN cp $(pwd)/redist/libmariadb.so.2 $(pwd)  
  
RUN chown -R ${TS3_USER}:${TS3_GROUP} ${TS3_HOME} && chmod u+x /entrypoint.sh  
  
USER ${TS3_USER}  
  
VOLUME ${TS3_HOME}  
  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
ENTRYPOINT /entrypoint.sh  

