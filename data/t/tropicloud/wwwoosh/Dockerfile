FROM alpine:3.2  
MAINTAINER admin@tropicloud.net  
  
ADD . /app  
RUN apk --update add bash netcat-openbsd  
  
EXPOSE 8080  
WORKDIR /app  
CMD bash app.sh  

