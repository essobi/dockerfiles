FROM benchflow/base-images:dev  
  
MAINTAINER Vincenzo FERME <info@vincenzoferme.it>  
  
ENV MONITOR_NAME cpu  
ENV MONITORS_VERSION v-dev  
  
RUN apk --update add wget && \  
wget -q --no-check-certificate -O /app/$MONITOR_NAME
https://github.com/benchflow/monitors/releases/download/$MONITORS_VERSION/$MONITOR_NAME
&& \  
chmod +x /app/$MONITOR_NAME && \  
apk del --purge wget && \  
rm -rf /var/cache/apk/*  
  
COPY ./services/300-cpu-monitor.conf /apps/chaperone.d/300-cpu-monitor.conf  
  
EXPOSE 8080

