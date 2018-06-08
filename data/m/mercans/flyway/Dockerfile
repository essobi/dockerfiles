FROM openjdk:8-jre-alpine  
  
COPY flyway /usr/local/lib/flyway  
  
RUN apk update && apk add --no-cache \  
bash \  
&& ln -s /usr/local/lib/flyway/flyway /usr/local/bin  
  
ENTRYPOINT ["flyway"]  
CMD ["-v"]  

