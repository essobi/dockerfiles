FROM benchflow/base-images:dev  
  
MAINTAINER Vincenzo FERME <info@vincenzoferme.it>  
  
ENV COLLECTOR_NAME mysql  
ENV COLLECTOR_VERSION v-dev  
  
#TODO: pin version of mysql-client  
RUN apk --update add wget gzip mysql-client && \  
wget -q --no-check-certificate -O /app/$COLLECTOR_NAME
https://github.com/benchflow/collectors/releases/download/$COLLECTOR_VERSION/$COLLECTOR_NAME
&& \  
chmod +x /app/$COLLECTOR_NAME && \  
apk del --purge wget && \  
rm -rf /var/cache/apk/*  
  
COPY ./services/300-dbms-mysql-collector.conf /apps/chaperone.d/300-dbms-
mysql-collector.conf  
  
EXPOSE 8080

