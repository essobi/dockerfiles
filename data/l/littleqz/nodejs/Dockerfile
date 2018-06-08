FROM alpine  
  
MAINTAINER littleqz@gmail.com  
LABEL description="A lightweight nodejs image with gulp and bower(based on
alpine linux)."  
RUN apk update && apk add bash fish nodejs  
  
RUN npm install -g gulp bower  
  
RUN sed -ri "/:1000/d" /etc/passwd /etc/group && \  
adduser -u 1000 -Dg me -s /usr/bin/fish -h /home/me me && \  
adduser me users  
  
USER me  
WORKDIR /var/www  
  
CMD bash  

