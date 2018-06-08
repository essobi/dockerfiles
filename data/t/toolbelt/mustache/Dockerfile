FROM alpine  
  
RUN apk --no-cache add ruby && { gem install mustache || true; }  
  
ENTRYPOINT [ "/usr/bin/mustache" ]  

