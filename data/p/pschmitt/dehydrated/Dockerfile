FROM python:alpine  
  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
ENV EMAIL=webmaster@example.com  
ENV KEY_ALGO=rsa  
ENV PROVIDER=SET_ME_ON_RUNTIME  
  
WORKDIR /app  
COPY docker-entrypoint.sh config /app/  
  
RUN apk add --no-cache openssl curl bash git && \  
pip install "git+https://github.com/pschmitt/lexicon.git@dev#egg=dns-
lexicon[namecheap]" && \  
curl
https://raw.githubusercontent.com/pschmitt/lexicon/dev/examples/dehydrated.default.sh
> /app/hook && \  
curl https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated
> /app/dehydrated && \  
chmod +x /app/hook /app/docker-entrypoint.sh /app/dehydrated && \  
apk del git  
  
VOLUME ["/data"]  
CMD ["/app/docker-entrypoint.sh"]  

