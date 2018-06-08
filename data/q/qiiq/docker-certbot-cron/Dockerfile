FROM certbot/certbot  
  
MAINTAINER Miroslav Spousta <qiq@ucw.cz>  
  
RUN apk add --no-cache netcat-openbsd  
  
ENV PROXY_CONTAINER_NAME=nginx  
ENV PROXY_DOMAINS=some.domain  
ENV EMAIL_ADDRESS=some@email  
ENV CERTBOT_ARGS=--test-cert  
  
COPY *.sh /  
  
ENTRYPOINT [ "/renew_certificates.sh" ]  

