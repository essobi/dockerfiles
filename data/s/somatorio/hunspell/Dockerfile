FROM alpine:3.5  
RUN apk add --no-cache hunspell hunspell-pt-br hunspell-en  
  
WORKDIR /workdir  
  
ENTRYPOINT ["/usr/bin/hunspell"]  

