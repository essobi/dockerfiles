FROM alpine:3.3  
RUN apk add --update openssl openssl-dev  
RUN wget https://github.com/muquit/mailsend/archive/1.19.tar.gz  
RUN apk add make gcc g++ \  
&& tar -zxvf 1.19.tar.gz \  
&& cd mailsend-1.19/ \  
&& ./configure --with-openssl=/usr \  
&& make clean \  
&& make install \  
&& rm -f ../1.19.tar.gz \  
&& apk del make gcc g++ && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["mailsend"]  

