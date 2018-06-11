FROM debian:jessie  
  
MAINTAINER Mykhailo Lieibenson <gramatron@gmail.com>  
  
ENV VIDEOBRIDGE_BUILDNUM="735"  
# These variables could be overridden to configure Prosody/ejabberd  
ENV VIDEOBRIDGE_SECRET="-secret-"  
ENV XMPP_DOMAIN="example.com"  
ENV XMPP_SUBDOMAIN="jitsi-videobridge"  
ENV XMPP_HOST="localhost"  
ENV XMPP_PORT="5275"  
ENV APIS="xmpp"  
ENV MEDIA_MIN_PORT="40000"  
ENV MEDIA_MAX_PORT="50000"  
# Install videobridge and dependencies  
USER root  
RUN apt-get update && apt-get -y install \  
wget \  
unzip \  
default-jre  
RUN wget https://download.jitsi.org/jitsi-videobridge/linux/jitsi-videobridge-
linux-x64-${VIDEOBRIDGE_BUILDNUM}.zip  
RUN unzip jitsi-videobridge-linux-x64-${VIDEOBRIDGE_BUILDNUM}.zip  
  
# Create videobridge user  
RUN mkdir /jvb && \  
groupadd -r jvb && \  
useradd -r -g jvb -d /jvb -s /sbin/nologin -c "Jitsi Videobridge User" jvb &&
\  
chown -R jvb:jvb /jvb  
  
# Configure and run  
USER jvb  
  
ADD conf/sip-communicator.properties /jvb/.sip-connumicator/sip-
communicator.properties  
ADD scripts/run.sh /jvb/run.sh  
  
EXPOSE 443 4443 $XMPP_PORT $MEDIA_MIN_PORT-$MEDIA_MAX_PORT  
  
CMD ["/jvb/run.sh"]  

