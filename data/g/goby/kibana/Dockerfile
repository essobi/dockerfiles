FROM alpine  
  
# Set environment variables  
ENV KIBANA_VERSION 4.6.4  
ENV PKG_NAME kibana  
ENV PKG_PLATFORM linux-x86_64  
ENV KIBANA_PKG $PKG_NAME-$KIBANA_VERSION-$PKG_PLATFORM  
ENV KIBANA_CONFIG
/opt/$PKG_NAME-$KIBANA_VERSION-$PKG_PLATFORM/config/kibana.yml  
ENV KIBANA_URL
https://download.elastic.co/$PKG_NAME/$PKG_NAME/$KIBANA_PKG.tar.gz  
ENV ELASTICSEARCH_HOST elasticsearch  
  
RUN addgroup -S kibana && adduser -S -G kibana kibana  
  
# Download Kibana  
RUN apk add --update ca-certificates wget nodejs \  
&& mkdir -p /opt \  
&& wget -O /tmp/$KIBANA_PKG.tar.gz $KIBANA_URL \  
&& tar -xvzf /tmp/$KIBANA_PKG.tar.gz -C /opt/ \  
&& ln -s /opt/$KIBANA_PKG /opt/$PKG_NAME \  
&& sed -i "s/localhost/$ELASTICSEARCH_HOST/" $KIBANA_CONFIG \  
&& rm -rf /tmp/*.tar.gz /var/cache/apk/* /opt/$KIBANA_PKG/node/ \  
&& mkdir -p /opt/$KIBANA_PKG/node/bin/ \  
&& ln -s $(which node) /opt/$PKG_NAME/node/bin/node \  
&& chown -R kibana:kibana /opt  
  
# Expose  
EXPOSE 5601  
# Add default config  
ADD kibana.yml /opt/kibana/config/kibana.yml  
  
USER kibana  
  
# Working directory  
WORKDIR ["/opt/kibana"]  
CMD ["/opt/kibana/bin/kibana"]  

