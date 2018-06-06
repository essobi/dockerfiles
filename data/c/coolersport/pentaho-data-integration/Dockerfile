FROM anapsix/alpine-java:8_jdk_unlimited  
  
MAINTAINER Tien Tran  
  
ENV TZ Australia/Melbourne  
  
COPY rootfs /  
  
RUN apk --no-cache --update add curl tzdata && \  
addgroup pentaho && \  
adduser -G pentaho -s /bin/sh -D pentaho && \  
echo "pentaho:$(date | md5sum | head -c 32)" | /usr/sbin/chpasswd && \  
curl -fsSL
https://nchc.dl.sourceforge.net/project/pentaho/Data%20Integration/7.1/pdi-
ce-7.1.0.0-12.zip -o /home/pentaho/pdi-ce.zip && \  
cd /home/pentaho && \  
unzip pdi-ce.zip && \  
rm -rf /home/pentaho/pdi-ce.zip && \  
chown -R pentaho:pentaho /home/pentaho/data-integration && \  
chmod u+x /entrypoint.sh && \  
rm -rf /apk /tmp/* /var/cache/apk/*  
  
WORKDIR /home/pentaho  
  
ENTRYPOINT ["/entrypoint.sh"]  
#CMD ["su", "-m", "-c", "/home/pentaho/data-integration/kitchen.sh",
"pentaho"]  

