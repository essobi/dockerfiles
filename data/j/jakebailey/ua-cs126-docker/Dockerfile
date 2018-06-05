FROM jakebailey/alpine-sane  
  
RUN apk --no-cache add \  
vim \  
&& adduser -D -s /bin/bash student  
  
USER student  
WORKDIR /home/student

