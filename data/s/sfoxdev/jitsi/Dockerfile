FROM ubuntu:16.04  
MAINTAINER SFoxDev <admin@sfoxdev.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
DOMAIN=sfoxdev.com \  
YOURSECRET1=jitsi \  
YOURSECRET2=jitsi \  
YOURSECRET3=jitsi \  
LC_ALL=C.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
#ARG REPOSITORY="https://download.jitsi.org/jitsi/debian"  
ARG REPOSITORY="https://download.jitsi.org/unstable"  
ARG VIDEOBRIDGE="989-1"  
ARG JICOFO="1.0-365-1"  
ARG JITSI="1.0.2230-1"  
ARG JITSI_MEET="1.0.2384-1"  
  
RUN apt-get update -y && apt-get install -y software-properties-common \  
&& add-apt-repository ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get install -y wget openjdk-8-jre nginx prosody luarocks default-jre-
headless curl mc \  
&& cd /tmp \  
&& wget -q ${REPOSITORY}/jitsi-videobridge_${VIDEOBRIDGE}_amd64.deb \  
&& dpkg -i jitsi-videobridge_${VIDEOBRIDGE}_amd64.deb \  
&& wget -q ${REPOSITORY}/jicofo_${JICOFO}_amd64.deb \  
&& dpkg -i jicofo_${JICOFO}_amd64.deb \  
&& wget -q ${REPOSITORY}/jitsi-meet-prosody_${JITSI}_all.deb \  
&& dpkg -i jitsi-meet-prosody_${JITSI}_all.deb \  
&& wget -q ${REPOSITORY}/jitsi-meet-web_${JITSI}_all.deb \  
&& dpkg -i jitsi-meet-web_${JITSI}_all.deb \  
&& wget -q ${REPOSITORY}/jitsi-meet-web-config_${JITSI}_all.deb \  
&& dpkg -i jitsi-meet-web-config_${JITSI}_all.deb \  
&& wget -q ${REPOSITORY}/jitsi-meet_${JITSI_MEET}_all.deb \  
&& dpkg -i jitsi-meet_${JITSI_MEET}_all.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir /root/samples \  
&& mkdir /var/run/prosody \  
&& chown prosody /var/run/prosody \  
&& touch /root/.first-boot \  
&& mkdir /keys \  
&& mkdir /recordings  
  
EXPOSE 80 443 5000 5222 5223 5269 5280 5281 5298 5247 10000-20000/udp  
  
COPY config /root/samples  
COPY run.sh run.sh  
  
VOLUME ["/keys","/recordings"]  
  
ENTRYPOINT ["./run.sh"]  

