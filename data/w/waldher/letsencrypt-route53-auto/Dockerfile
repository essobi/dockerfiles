FROM alpine:3.5  
RUN apk add --no-cache py-pip bash curl  
RUN pip install dns-lexicon[route53]  
  
WORKDIR /work  
  
RUN apk add --no-cache openssl  
RUN wget -q https://github.com/lukas2511/dehydrated/raw/master/dehydrated  
RUN chmod +x dehydrated  
RUN wget -q
https://github.com/AnalogJ/lexicon/raw/master/examples/dehydrated.default.sh  
RUN chmod +x dehydrated.default.sh  
ADD entrypoint.sh .  
  
VOLUME "/work/certs"  
VOLUME "/work/accounts"  
  
ENTRYPOINT ["./entrypoint.sh"]  

