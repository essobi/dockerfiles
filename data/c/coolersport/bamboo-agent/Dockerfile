FROM coolersport/maven:3.2.5-jdk-8  
  
COPY run-agent.sh /tmp/  
  
RUN apk add \--update wget \  
&& addgroup alpine && adduser -G alpine -s /bin/sh -D alpine \  
&& mv /tmp/run-agent.sh /home/alpine \  
&& chown alpine /home/alpine/run-agent.sh \  
&& rm -rf /apk /tmp/* /var/cache/apk/*  
  
USER alpine  
WORKDIR /home/alpine  
  
RUN wget --no-check-certificate -O /home/alpine/bamboo-update-capability.sh
https://bitbucket.org/atlassian/bamboo-update-capability/raw/master/bamboo-
update-capability.sh \  
&& chmod +x /home/alpine/bamboo-update-capability.sh \  
&& mkdir -p /home/alpine/bamboo-agent-home/bin \  
&& /home/alpine/bamboo-update-capability.sh "Oracle JDK 1.8" /opt/jdk1.8.0_144
\  
&& chmod +x /home/alpine/run-agent.sh  
  
CMD ["/home/alpine/run-agent.sh"]  

