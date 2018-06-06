  
FROM alpine:3.7  
ENV PLUGINS_DIR /opt/sonarqube/extensions/plugins  
  
RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/main" >
/etc/apk/repositories && \  
echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/community" >>
/etc/apk/repositories && \  
echo "https://mirror.tuna.tsinghua.edu.cn/alpine/edge/testing/" >>
/etc/apk/repositories && \  
apk --no-cache add --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community bash wget aria2 ca-certificates && \  
rm -rf /tmp/* /var/cache/apk/*  
  
# Copy the plugin (jar file) to $SONAR_INSTALL_DIR/extensions/plugins  
WORKDIR $PLUGINS_DIR  
COPY docker/plugins.sh /opt/sonarqube/extensions/plugins/plugins.sh  
COPY docker/plugins.txt /opt/sonarqube/extensions/plugins/plugins.txt  
RUN /opt/sonarqube/extensions/plugins/plugins.sh
/opt/sonarqube/extensions/plugins/plugins.txt  
VOLUME $PLUGINS_DIR  
  
CMD ls -asl $PLUGINS_DIR  

