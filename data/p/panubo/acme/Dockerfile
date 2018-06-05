FROM alpine:latest  
  
ENV ACME_TINY_GIT_HASH=4ed13950c0a9cf61f1ca81ff1874cde1cf48ab32  
  
RUN apk add --update bash curl openssl python && \  
rm -rf /var/cache/apk/*  
  
ADD https://raw.githubusercontent.com/diafygi/acme-
tiny/${ACME_TINY_GIT_HASH}/acme_tiny.py /  
  
RUN chmod +x /*.py  
  
COPY run.sh /  
  
ENTRYPOINT ["/run.sh"]  
  

