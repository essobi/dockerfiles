FROM davimss/openjdk-alpine:8  
WORKDIR /opt  
  
ENV INSTALLPROP opendj-install.properties  
ENV OPENDJ_FILE OpenDJ-3.0.0.zip  
  
COPY $INSTALLPROP /opt/$INSTALLPROP  
  
USER root  
  
RUN set -x ; \  
apk add --no-cache --virtual .tmp-deps curl ; \  
curl -o /opt/$OPENDJ_FILE -fSL
https://github.com/OpenRock/OpenDJ/releases/download/3.0.0/OpenDJ-3.0.0.zip ;
\  
unzip /opt/$OPENDJ_FILE ; \  
rm -f /opt/$OPENDJ_FILE ; \  
apk del .tmp-deps ; \  
apk del curl ; \  
rm -rf /var/cache/apk/* ; \  
chown -Rf caos:caos /opt/*  
  
USER caos  
  
WORKDIR /opt/opendj  
  
RUN ./setup --cli --propertiesFilePath /opt/$INSTALLPROP \--acceptLicense
--no-prompt  
  
RUN ./bin/status  
  
EXPOSE 4444 1389 1636  
COPY lib/template-virtual-attribute.jar /opt/opendj/lib/extensions/template-
virtual-attribute.jar  
COPY lib/template-virtual-attribute.ldif
/opt/opendj/config/schema/99-template-virtual-attribute.ldif  
  
CMD ["/opt/opendj/bin/start-ds", "-N"]  

