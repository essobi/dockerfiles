  
#####################  
FROM nginx:1.11.6-alpine  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
  
#####################  
RUN apk update && apk add wget  
WORKDIR /usr/share/nginx/html  
  
# ENV SWAGGER_VERSION master  
ENV SWAGGER_VERSION 2.2.8  
# not for master  
ENV SWAGGER_ID v$SWAGGER_VERSION  
  
ENV SWAGGER_MASTER https://github.com/swagger-api/swagger-
ui/archive/$SWAGGER_ID.zip  
# ENV SWAGGER_MASTER https://github.com/swagger-api/swagger-
ui/archive/master.zip  
RUN wget --no-check-certificate -q $SWAGGER_MASTER \  
&& unzip $SWAGGER_ID.zip \  
&& mv swagger-ui-$SWAGGER_VERSION/dist swagger-ui \  
&& rm -rf swagger-ui-$SWAGGER_ID  

