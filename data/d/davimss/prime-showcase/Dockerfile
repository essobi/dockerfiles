FROM davimss/tomcat-alpine:8.5.20  
  
RUN set -x ; \  
apk add --no-cache --virtual .tmp-deps curl ; \  
curl -o $CATALINA_HOME/webapps/showcase-6.1.war -L
https://www.dropbox.com/s/etsxyul1mc9txgn/showcase-6.1.war?dl=1 ; \  
apk del .tmp-deps ; \  
apk del curl ; \  
rm -rf /var/cache/apk/*

