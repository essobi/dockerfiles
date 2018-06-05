from traefik:1.6.2-alpine  
  
LABEL maintainer="Burak Ince <burak.ince@linux.org.tr>"  
  
ENV RSYSLOG_VERSION=8.35.0-r0 \  
SUPERVISOR_VERSION=3.2.4-r0  
  
RUN cd /etc/apk/keys \  
&& wget http://alpine.adiscon.com/rsyslog@lists.adiscon.com-5a55e598.rsa.pub \  
&& echo 'http://alpine.adiscon.com/3.7/stable' >> /etc/apk/repositories \  
&& apk update \  
&& apk add --no-cache supervisor=$SUPERVISOR_VERSION rsyslog=$RSYSLOG_VERSION
\  
&& rm -rf /var/cache/apk/*  

