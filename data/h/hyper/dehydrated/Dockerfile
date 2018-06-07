FROM alpine  
RUN apk add --update openssl curl bash \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /usr/local/bin  
RUN curl
https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated >
./dehydrated  
RUN chmod +x ./dehydrated  
ENTRYPOINT ["dehydrated"]  

