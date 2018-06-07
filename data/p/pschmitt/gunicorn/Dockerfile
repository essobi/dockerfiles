FROM alpine:3.3  
RUN apk --update add py-gunicorn python py-pip  
COPY start.sh /usr/bin/start.sh  
  
VOLUME /app  
WORKDIR /app  
  
ENV APP=bot:app  
EXPOSE 8000  
ENTRYPOINT /usr/bin/start.sh  

