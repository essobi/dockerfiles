FROM oconnormi/ddf-base  
MAINTAINER oconnormi  
  
ENV APP_VERSION=0.2.2  
ENV APP_BASE=/opt  
ENV APP_HOME=$APP_BASE/alliance  
ENV APP_LOG=$APP_HOME/data/log/ddf.log  
#releases, snapshots  
ENV APP_REPO=releases  
ENV STARTUP_APPS=admin-app;platform-app;catalog-app;spatial-app;security-
services-app;security-app  
ENV UNINSTALL_FEATURES=admin-modules-installer  
  
RUN apk add --no-cache curl unzip  
  
RUN mkdir -p $APP_BASE/tmp \  
&& mkdir -p $APP_HOME \  
&& cd $APP_BASE/tmp \  
&& curl -o alliance.sha1
"http://artifacts.codice.org/service/local/artifact/maven/content?g=org.codice.alliance.distribution&a=alliance&v=$APP_VERSION&r=$APP_REPO&e=zip.sha1"
\  
&& sed -i'' -e '/^/ s/$/ alliance.zip/' alliance.sha1 \  
&& curl -o alliance.zip
"http://artifacts.codice.org/service/local/artifact/maven/content?g=org.codice.alliance.distribution&a=alliance&v=$APP_VERSION&r=$APP_REPO&e=zip"
\  
&& sha1sum -c alliance.sha1 2>&1 > /dev/null \  
&& rm alliance.sha1 \  
&& unzip alliance.zip \  
&& mv alliance-${APP_VERSION}/* $APP_HOME \  
&& rm -rf $APP_BASE/tmp  
  
VOLUME $APP_HOME/data $APP_HOME/deploy $APP_HOME/etc  
  
EXPOSE 8101 8993 8181  

