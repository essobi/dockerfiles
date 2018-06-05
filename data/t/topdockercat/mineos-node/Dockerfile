FROM ubuntu  
MAINTAINER TopCat <topmailcat@googlemail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV MINEOS_VERSION v1.1.7  
ENV VERSION 8  
ENV UPDATE 131  
ENV BUILD 11  
ENV SIG d54c1d3a095b4ff2b6607d096fa80163  
  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
ENV JRE_HOME ${JAVA_HOME}/jre  
  
ENV OPENSSL_VERSION 1.0.2j  
  
# update system  
RUN apt-get update && apt-get upgrade -y  
  
# update and accept all prompts  
RUN apt-get update && apt-get install -y \  
supervisor \  
rdiff-backup \  
screen \  
rsync \  
git \  
curl \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# intall java  
RUN apt-get update && apt-get install ca-certificates \  
gcc \  
libc6-dev libssl-dev make \  
-y --no-install-recommends  
  
RUN curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/"${SIG}"/jre-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz
\  
| tar xz -C /tmp && \  
mkdir -p /usr/lib/jvm && mv /tmp/jre1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" &&
\  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GlobalSign_Root_CA.pem \  
https://www.openssl.org/source/openssl-"${OPENSSL_VERSION}".tar.gz \  
| tar xz -C /tmp && \  
cd /tmp/openssl-"${OPENSSL_VERSION}" && \  
./config --prefix=/usr && \  
make clean && make && make install && \  
apt-get remove --purge --auto-remove -y \  
gcc \  
libc6-dev \  
libssl-dev \  
make && \  
apt-get autoclean && apt-get --purge -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JAVA_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --set java "${JAVA_HOME}/bin/java" && \  
update-alternatives --set javaws "${JAVA_HOME}/bin/javaws"  
  
#install node from nodesource  
RUN curl
https://deb.nodesource.com/node_4.x/pool/main/n/nodejs/nodejs_4.6.2-1nodesource1~jessie1_amd64.deb
> node.deb \  
&& dpkg -i node.deb \  
&& rm node.deb  
  
#download mineos from github  
RUN mkdir /usr/games/minecraft \  
&& cd /usr/games/minecraft \  
&& git clone https://github.com/hexparrot/mineos-node.git . \  
&& git checkout tags/"${MINEOS_VERSION}" -b release \  
&& chmod +x webui.js mineos_console.js service.js  
  
#build npm deps and clean up apt for image minimalization  
RUN cd /usr/games/minecraft \  
&& apt-get update \  
&& apt-get install -y build-essential \  
&& npm install \  
&& apt-get remove --purge -y build-essential \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#configure and run supervisor  
RUN cp /usr/games/minecraft/init/supervisor_conf
/etc/supervisor/conf.d/mineos.conf  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  
  
#entrypoint allowing for setting of mc password  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8443 25565-25570  
VOLUME /var/games/minecraft  

