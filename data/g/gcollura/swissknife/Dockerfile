FROM alpine:latest  
MAINTAINER Giulio Collura <giulio.collura@gmail.com>  
  
RUN apk add --update zsh curl && \  
rm -rf /var/cache/apk/*  
  
COPY zshrc /root/.zshrc  
  
CMD ["/bin/zsh"]  

