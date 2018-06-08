FROM alpine:edge  
  
RUN apk --no-cache add monit=5.24.0-r1  
  
VOLUME /etc/monit.d/  
  
EXPOSE 2812  
CMD ["monit", "-I", "-B"]

