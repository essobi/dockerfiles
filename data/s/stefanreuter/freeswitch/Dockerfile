FROM debian:jessie  
MAINTAINER Stefan Reuter <docker@reucon.com>  
  
RUN set -x \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
curl \  
&& curl -Ls http://files.freeswitch.org/repo/deb/freeswitch-1.6/key.gpg | apt-
key add - \  
&& echo "deb http://files.freeswitch.org/repo/deb/freeswitch-1.6/ jessie main"
\  
> /etc/apt/sources.list.d/freeswitch.list \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
freeswitch-all \  
libyuv \  
vorbis-tools \  
xmlstarlet \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes  
  
  
# Used for SIP signaling (Standard SIP Port, for default Internal Profile)  
EXPOSE 5060/tcp 5060/udp  
  
# Used for SIP signaling (For default "External" Profile)  
EXPOSE 5080/tcp 5080/udp  
  
# Used for WebRTC (Websocket)  
EXPOSE 5066/tcp 7443/tcp  
  
# Used for Verto  
EXPOSE 8081/tcp 8082/tcp  
  
# Used for mod_event_socket * (ESL)  
EXPOSE 8021/tcp  
  
# Used for audio/video data in SIP and other protocols (RTP/ RTCP multimedia
streaming)  
EXPOSE 64535-65535/udp  
  
CMD [ "/usr/bin/freeswitch", "-nf", "-nc" ]  

