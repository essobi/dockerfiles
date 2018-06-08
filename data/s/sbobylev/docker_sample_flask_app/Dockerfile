FROM alpine:latest  
MAINTAINER sbobylev <stas.bobylev@gmail.com>  
  
RUN apk --update upgrade && \  
apk add --no-cache python py-flask && \  
mkdir /app && \  
rm -rf /var/cache/apk/*  
  
COPY src/app.py /app  
  
WORKDIR /app  
  
EXPOSE 8080  
ENTRYPOINT ["python", "app.py"]  

