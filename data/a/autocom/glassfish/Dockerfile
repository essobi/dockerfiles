FROM autocom/jdk:8  
ENV GLASSFISH_VERSION 4.1.2  
ENV GLASSFISH_SHA256SUM
68d5c0d95152a07e68e9b00535b11e7b8727646eb8bca05f918abdadebac7266  
ENV GLASSFISH_DOMAINDIR /var/lib/glassfish/domains  
  
RUN groupadd -r glassfish && useradd -d /home/glassfish -m -r -g glassfish
glassfish  
  
RUN apt-get update && apt-get install -y curl unzip expect sudo --no-install-
recommends \  
&& curl -SL
"http://download.java.net/glassfish/$GLASSFISH_VERSION/release/glassfish-$GLASSFISH_VERSION.zip"
-o glassfish.zip \  
&& echo "$GLASSFISH_SHA256SUM glassfish.zip" | sha256sum -c /dev/stdin \  
&& unzip -d /opt glassfish.zip \  
&& mv /opt/glassfish4 /opt/glassfish \  
&& mkdir -p $GLASSFISH_DOMAINDIR \  
&& chown -R glassfish:glassfish $GLASSFISH_DOMAINDIR \  
&& rm glassfish.zip \  
&& apt-get purge -y --auto-remove curl unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH $PATH:/opt/glassfish/bin  
  
WORKDIR /opt/glassfish  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 4848 8080 8181  
CMD ["/bin/sh", "-c", "sudo PATH=$PATH -u glassfish /usr/bin/env asadmin
start-domain -v --domaindir $GLASSFISH_DOMAINDIR $GLASSFISH_DOMAIN"]  

