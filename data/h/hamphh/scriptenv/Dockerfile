FROM debian:jessie  
MAINTAINER hamphh <docker@hampelhh.de>  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV HOME /root  
  
# User für unraid  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody  
  
# UTF-8  
RUN apt-get update && \  
apt-get install -y locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8 && \  
apt-get remove -y locales  
ENV LANG C.UTF-8  
# Timezone  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Python, ffmpeg ufraw  
RUN apt-get update -qq && \  
echo deb http://www.deb-multimedia.org jessie main non-free
>>/etc/apt/sources.list && \  
apt-get update -qq && \  
apt-get install -qy --force-yes deb-multimedia-keyring && \  
apt-get update -qq && \  
apt-get install -qy python3 python3-requests ffmpeg ufraw-batch  
  
ENV JRE_VERSION jre1.8.0_60  
ENV JRE_FILE jre-8u60-linux-x64.tar.gz  
ENV JRE_URL http://download.oracle.com/otn-pub/java/jdk/8u60-b27/${JRE_FILE}  
  
# Install Java  
RUN apt-get install -qy wget && cd /tmp && \  
wget -q --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" ${JRE_URL} && \  
tar xzvf ${JRE_FILE} && mkdir /opt/Oracle_Java && cp -r ${JRE_VERSION}
/opt/Oracle_Java/${JRE_VERSION} && \  
update-alternatives --install "/usr/bin/java" "java"
"/opt/Oracle_Java/${JRE_VERSION}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"/opt/Oracle_Java/${JRE_VERSION}/bin/javaws" 1 && \  
update-alternatives --set "java" "/opt/Oracle_Java/${JRE_VERSION}/bin/java" &&
\  
update-alternatives --set "javaws"
"/opt/Oracle_Java/${JRE_VERSION}/bin/javaws"  
  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Clean up  
RUN apt-get purge -qq wget && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
VOLUME /data \  
/scripts \  
/logs  
  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
  
ENTRYPOINT ["/root/run.sh"]  
CMD ["--version"]  

