FROM openjdk:8-jre-slim  
MAINTAINER Jacek Kowalski <Jacek@jacekk.info>  
  
ENV UNIFI_VERSION 5.7.23  
  
RUN apt-get update \  
&& apt-get -y install \  
wget jsvc mongodb-server libcap2 binutils procps sudo \  
&& apt-get -y clean \  
&& rm -Rf /var/lib/apt/lists/*  
  
RUN cd /tmp \  
&& wget
"https://www.ubnt.com/downloads/unifi/${UNIFI_VERSION}/unifi_sysvinit_all.deb"
\  
&& groupadd -r -g 500 unifi \  
&& useradd -r -d /usr/lib/unifi -u 500 -g 500 unifi \  
&& dpkg -i unifi_sysvinit_all.deb \  
&& rm -rf unifi_sysvinit_all.deb /var/lib/unifi/* \  
&& mkdir -p /usr/lib/unifi/data /var/lib/unifi \  
&& chown -Rf unifi:unifi /usr/lib/unifi /var/lib/unifi  
  
EXPOSE 8080 8443 8843 8880  
  
VOLUME /usr/lib/unifi/data  
  
WORKDIR /var/lib/unifi  
COPY run.sh /run.sh  
CMD /run.sh  
  
USER unifi  
  
HEALTHCHECK --start-period=3m CMD wget -q -O /dev/null --no-check-certificate
\  
https://127.0.0.1:8443/manage/account/login  

