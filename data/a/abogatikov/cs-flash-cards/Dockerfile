FROM golang:1.8.0-alpine  
  
  
RUN apk update \  
&& apk add ca-certificates wget curl \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /opt  
RUN wget $(curl -X GET "https://api.github.com/repos/abogatikov/cs-flash-
cards/releases/latest" | grep browser_ | grep cs-flash-cards- | cut -d\" -f4)
-O ./cs-flash-cards.tar.gz \  
&& tar -C ./ -zxvf cs-flash-cards.tar.gz \  
&& rm -rf ./cs-flash-cards.tar.gz  
  
WORKDIR /opt/cs-flash-cards  
EXPOSE 8080  
ENTRYPOINT ["./cs-flash-cards"]

