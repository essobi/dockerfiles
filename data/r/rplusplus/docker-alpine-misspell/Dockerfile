FROM alpine:3.7  
  
RUN apk add \--no-cache curl && \  
apk add \--no-cache git && \  
apk add \--no-cache --update openssh && \  
rm -rf /var/cache/apk/* && \  
curl -L https://git.io/misspell | sh && \  
mv ./bin/misspell /usr/local/bin/ && \  
misspell -v  
  
CMD ["misspell"]  

