FROM java:latest  
  
MAINTAINER Balazs Mazas <mazasb@gmail.com>  
  
ENV APP_VERSION 2.0  
ENV APP_BUILD $APP_VERSION.314  
ENV APP_DIST hub-ring-bundle-$APP_BUILD  
ENV APP_DISTFILE $APP_DIST.zip  
ENV APP_PREFIX /opt  
ENV APP_DIR $APP_PREFIX/hub  
ENV APP_HOME /data  
ENV APP_USER hub  
ENV APP_PORT 8080  
WORKDIR $APP_PREFIX  
  
RUN wget -q https://download.jetbrains.com/hub/$APP_VERSION/$APP_DISTFILE && \  
unzip -q $APP_DISTFILE && \  
mv $APP_DIST $APP_DIR && \  
rm -f $APP_DISTFILE && \  
rm -rf internal/java  
  
WORKDIR $APP_DIR  
  
COPY run.sh .  
RUN mkdir $APP_HOME && \  
groupadd -r -g 2000 $APP_USER && \  
useradd -r -g $APP_USER -u 2000 -d $APP_HOME $APP_USER && \  
chmod o+rx run.sh && \  
chown -R $APP_USER:$APP_USER $APP_HOME $APP_DIR  
  
USER $APP_USER  
ENTRYPOINT ["./run.sh"]  
EXPOSE $APP_PORT  
VOLUME ["$APP_HOME"]  

