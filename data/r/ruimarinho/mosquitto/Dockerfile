FROM alpine:edge  
  
MAINTAINER Rui Marinho <ruipmarinho@gmail.com> (@ruimarinho)  
  
RUN adduser -S mosquitto  
  
RUN apk add --no-cache mosquitto-clients~1.4.14 mosquitto~1.4.14 su-exec  
  
EXPOSE 1883 9001  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["mosquitto"]  

