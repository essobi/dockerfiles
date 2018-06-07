FROM openjdk:8-jre-alpine  
  
RUN apk update \  
&& apk upgrade \  
&& apk add \--no-cache --update curl ca-certificates openssl perl \  
&& adduser -D -h /home/container container  
  
USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./start.sh /start.sh  
  
CMD ["/bin/ash", "/start.sh"]

