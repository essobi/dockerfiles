FROM philippwaller/java:latest  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="OpenHAB" \  
org.label-schema.description="OpenHAB"  
  
ENV JAVA_PERM_MEM=1024 \  
JAVA_MAX_PERM_MEM=1024 \  
OPENHAB_URL=https://openhab.ci.cloudbees.com/job/openHAB-
Distribution/lastBuild/artifact/distributions/openhab/target/openhab-2.2.0-SNAPSHOT.tar.gz
\  
OPENHAB_HOME=/opt/openhab \  
OPENHAB_USER=openhab \  
OPENHAB_HTTP_PORT=8080 \  
OPENHAB_HTTPS_PORT=8443 \  
OPENHAB_USERID=9100 \  
OPENHAB_GROUP=openhab \  
OPENHAB_GROUPID=9100  
  
RUN mkdir -p $OPENHAB_HOME \  
&& curl -L -o /tmp/openhab.tar.gz $OPENHAB_URL \  
&& tar -xzf /tmp/openhab.tar.gz -C $OPENHAB_HOME \  
&& rm /tmp/openhab.tar.gz \  
&& mkdir -p /home/openhab \  
&& groupadd -g $OPENHAB_GROUPID $OPENHAB_GROUP \  
&& useradd -d /home/openhab -g $OPENHAB_GROUPID -u $OPENHAB_USERID
$OPENHAB_USER \  
&& chown -hR $OPENHAB_USER:$OPENHAB_GROUP $OPENHAB_HOME /home/openhab  
  
EXPOSE 8080:8080 8443:8443 9125:9125 9126:9126  
  
COPY overlay/entrypoint.sh /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

