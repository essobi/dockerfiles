FROM alpine:3.3  
RUN apk add --update curl sudo python  
RUN curl -s
https://raw.githubusercontent.com/Shopify/themekit/master/scripts/install |
sudo python  
RUN apk del curl sudo && rm -rf /var/cache/apk/* && mkdir /theme  
WORKDIR /theme  
  
ENTRYPOINT ["/usr/local/bin/theme"]  

