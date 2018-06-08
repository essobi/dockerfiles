## -*- docker-image-name: "mcreations/nexus" -*-  
#  
# Nexus 3 Container  
#  
# Dependencies:  
#  
# Volume: /data  
#  
FROM mcreations/openwrt-java:8  
MAINTAINER Kambiz Darabi <darabi@m-creations.net>  
  
ENV APP_VERSION 3.0.1-01  
ENV APP_ARCHIVE nexus-${APP_VERSION}-unix.tar.gz  
  
ENV NEXUS_DATA /data/nexus-work  
VOLUME /data  
  
EXPOSE 8081  
ENV JAVA_MAX_MEM 1200m  
ENV JAVA_MIN_MEM 1200m  
ENV EXTRA_JAVA_OPTS ""  
ENV NEXUS_UID 200  
ENV NEXUS_GID 200  
ADD image/root /  
  
RUN opkg update && opkg install shadow-useradd shadow-groupadd coreutils-stat
&&\  
groupadd -g ${NEXUS_GID} nexus &&\  
useradd -u ${NEXUS_UID} -g ${NEXUS_GID} \--home-dir /opt/nexus --no-create-
home nexus --shell /bin/false &&\  
opkg --force-removal-of-dependent-packages remove libiconv-full libintl-full
&&\  
rm /tmp/opkg-lists/* &&\  
wget --progress dot:giga https://download.sonatype.com/nexus/3/${APP_ARCHIVE}
&&\  
tar xzf ${APP_ARCHIVE} &&\  
rm ${APP_ARCHIVE} &&\  
mv nexus-${APP_VERSION} /opt/nexus &&\  
sed -e "s|karaf.home=.|karaf.home=/opt/nexus|g" \  
-e "s|karaf.base=.|karaf.base=/opt/nexus|g" \  
-e "s|karaf.etc=etc|karaf.etc=/opt/nexus/etc|g" \  
-e "s|java.util.logging.config.file=etc|java.util.logging.config.file=/opt/nexus/etc|g" \  
-e "s|karaf.data=data|karaf.data=${NEXUS_DATA}|g" \  
-e "s|java.io.tmpdir=data/tmp|java.io.tmpdir=${NEXUS_DATA}/tmp|g" \  
-i /opt/nexus/bin/nexus.vmoptions &&\  
chown -R nexus:nexus /opt/nexus  
  
CMD /nexus  

