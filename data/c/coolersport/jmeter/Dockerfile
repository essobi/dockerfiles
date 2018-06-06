FROM anapsix/alpine-java:8_jdk_unlimited  
  
MAINTAINER Tien Tran  
  
ADD /apk /apk  
  
RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys \  
&& apk --no-cache --update add /apk/x11vnc-0.9.13-r0.apk \  
&& apk --no-cache add openssl xvfb openbox xfce4-terminal supervisor sudo tar
curl \  
# add alpine user with random password  
&& addgroup alpine \  
&& adduser -G alpine -s /bin/sh -D alpine \  
&& echo "alpine:$(date | md5sum | head -c 32)" | /usr/sbin/chpasswd \  
&& echo "alpine ALL=(ALL) ALL" >> /etc/sudoers \  
# clean up apk cache  
&& rm -rf /apk /tmp/* /var/cache/apk/* \  
# install jmeter  
&& curl -fsSLO https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-3.2.tgz \  
&& mkdir /opt/jmeter \  
&& tar --strip-components=1 -xvzf apache-jmeter-3.2.tgz -C /opt/jmeter \  
&& rm -rf apache-jmeter-3.2.tgz \  
&& ln -s /opt/jmeter/bin/jmeter /usr/bin/jmeter \  
# add websocket sampler  
&& curl -fsSL https://bitbucket.org/coolersport/jmeter-websocket-
samplers/downloads/JMeterWebSocketSamplers-0.10-20170908.jar -o
/opt/jmeter/lib/ext/JMeterWebSocketSamplers-0.10-20170908.jar \  
# add minimal-json library  
&& curl -fsSL https://github.com/ralfstx/minimal-
json/releases/download/0.9.4/minimal-json-0.9.4.jar -o
/opt/jmeter/lib/ext/minimal-json-0.9.4.jar \  
# upgrade groovy  
&& rm -rf /opt/jmeter/lib/groovy* \  
&& curl -fsSL https://repo1.maven.org/maven2/org/codehaus/groovy/groovy-
all/2.4.12/groovy-all-2.4.12.jar -o /opt/jmeter/lib/groovy-all-2.4.12.jar  
  
ADD etc /etc  
  
WORKDIR /home/alpine  
USER alpine  
  
ENV RESOLUTION 1280x720x24  
  
EXPOSE 5900  
  
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  

