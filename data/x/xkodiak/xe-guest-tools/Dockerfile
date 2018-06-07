FROM golang:alpine  
MAINTAINER xkodiak  
  
WORKDIR /  
RUN apk update && apk add git make  
RUN git clone https://github.com/xenserver/xe-guest-utilities.git /tmp/xe-
guest-utilities  
RUN make --directory=/tmp/xe-guest-utilities build && cp -R /tmp/xe-guest-
utilities/build/stage/* / && rm -R /tmp/*  
  
COPY assets/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["bash", "entrypoint.sh"]

