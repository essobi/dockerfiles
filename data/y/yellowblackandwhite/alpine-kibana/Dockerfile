FROM yellowblackandwhite/alpine-base  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
# Set environment variables  
ENV KIBANA_VERSION 4.5.1  
ENV PKG_NAME kibana  
ENV PKG_PLATFORM linux-x64  
ENV KIBANA_PKG $PKG_NAME-$KIBANA_VERSION-$PKG_PLATFORM  
ENV KIBANA_CONFIG
/opt/$PKG_NAME-$KIBANA_VERSION-$PKG_PLATFORM/config/kibana.yml  
ENV KIBANA_URL
https://download.elastic.co/$PKG_NAME/$PKG_NAME/$KIBANA_PKG.tar.gz  
ENV ELASTICSEARCH_HOST elasticsearch  
ENV PATH /opt/kibana/bin:$PATH  
# Download Kibana  
RUN apk update \  
&& apk add ca-certificates curl nodejs \  
&& mkdir -p /opt \  
&& curl -o /tmp/$KIBANA_PKG.tar.gz $KIBANA_URL \  
&& tar -xvzf /tmp/$KIBANA_PKG.tar.gz -C /opt/ \  
&& ln -s /opt/$KIBANA_PKG /opt/$PKG_NAME \  
&& sed -ri "s!^(\\#\s*)?(elasticsearch\\.url:).*!\2
'http://elasticsearch:9200'!" $KIBANA_CONFIG \  
&& grep -q 'elasticsearch:9200' $KIBANA_CONFIG \  
&& rm -rf /tmp/*.tar.gz /var/cache/apk/* /opt/$KIBANA_PKG/node/ \  
&& mkdir -p /opt/$KIBANA_PKG/node/bin/ \  
&& ln -s $(which node) /opt/$PKG_NAME/node/bin/node \  
&& chown -R 1000:1000 /opt/$PKG_NAME-$KIBANA_VERSION-$PKG_PLATFORM  
# Expose  
# Working directory  
EXPOSE 5601  
COPY entrypoint.sh /  
USER alpine  
WORKDIR ["/opt/$KIBANA_PKG"]  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["kibana"]  

