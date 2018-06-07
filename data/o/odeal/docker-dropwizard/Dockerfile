FROM openjdk:8-jre-alpine  
  
RUN mkdir -p /srv/www/ode.al/service  
# COPY target/service.jar /srv/www/ode.al/service/service.jar  
# COPY config.yaml /srv/www/ode.al/service/config.yaml  
RUN apk add \--update tzdata  
RUN cp /usr/share/zoneinfo/Europe/Istanbul /etc/localtime  
RUN echo "Europe/Istanbul" > /etc/timezone  
RUN apk del tzdata  
  
EXPOSE 8080 8081  
  
ENTRYPOINT java -jar /srv/www/ode.al/service/service.jar server
/srv/www/ode.al/service/config.yaml  

