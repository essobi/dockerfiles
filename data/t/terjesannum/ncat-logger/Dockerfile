FROM alpine:3.6  
LABEL maintainer "terje@offpiste.org"  
  
RUN apk add --update nmap-ncat && rm -rf /var/cache/apk/*  
  
EXPOSE 4000  
CMD ["ncat", "-k", "-l", "4000"]  

