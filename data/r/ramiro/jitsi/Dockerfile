FROM ubuntu:trusty  
MAINTAINER rberrelleza@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use https://download.jitsi.org/unstable/ for unstable  
ARG REPOSITORY="https://download.jitsi.org/jitsi/debian"  
# Latest stable as of 11/24  
ARG JITSI="1.0.1073-1"  
ARG VIDEOBRIDGE="751-1"  
ARG JICOFO="1.0-267-1"  
RUN apt-get update -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y wget openjdk-8-jre nginx prosody luarocks default-jre-
headless  
  
RUN cd /tmp && \  
wget -q ${REPOSITORY}/jitsi-videobridge_${VIDEOBRIDGE}_amd64.deb && \  
dpkg -i jitsi-videobridge_${VIDEOBRIDGE}_amd64.deb && \  
wget -q ${REPOSITORY}/jicofo_${JICOFO}_amd64.deb && \  
dpkg -i jicofo_${JICOFO}_amd64.deb && \  
wget -q ${REPOSITORY}/jitsi-meet-prosody_${JITSI}_all.deb && \  
dpkg -i jitsi-meet-prosody_${JITSI}_all.deb && \  
wget -q ${REPOSITORY}/jitsi-meet_${JITSI}_all.deb && \  
dpkg -i jitsi-meet_${JITSI}_all.deb  
  
RUN apt-get clean && \  
mkdir /root/samples && \  
mkdir /var/run/prosody && \  
chown prosody /var/run/prosody && \  
touch /root/.first-boot && \  
mkdir /keys && \  
mkdir /recordings  
  
EXPOSE 80 443  
EXPOSE 10000-20000/udp  
  
COPY config /root/samples  
COPY run.sh run.sh  
  
ENV DOMAIN jitsi.example.com  
ENV YOURSECRET1 jitsi  
ENV YOURSECRET2 jitsi  
ENV YOURSECRET3 jitsi  
  
VOLUME /keys  
VOLUME /recordings  
  
ENTRYPOINT ./run.sh  
  

