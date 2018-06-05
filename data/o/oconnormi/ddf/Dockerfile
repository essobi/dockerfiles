FROM alpine  
ENV DDF_VERSION=2.11.4  
RUN apk add --no-cache curl unzip  
RUN curl -o ddf.zip \  
"http://artifacts.codice.org/service/local/artifact/maven/content?g=org.codice.ddf&a=ddf&v=$DDF_VERSION&r=releases&e=zip"  
RUN unzip ddf.zip  
RUN mv ddf-${DDF_VERSION} /ddf  
  
FROM oconnormi/ddf-base:2.11-alpine  
LABEL maintainer=oconnormi  
  
ENV APP_HOME=/app  
ENV APP_NAME=ddf  
ENV APP_LOG=$APP_HOME/data/log/$APP_NAME.log  
  
COPY \--from=0 /ddf $APP_HOME  
  
VOLUME $APP_HOME/data $APP_HOME/deploy $APP_HOME/etc  
  
EXPOSE 8101 8993 8181  

