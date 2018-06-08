FROM alpine:3.4  
MAINTAINER https://github.com/PengBAI/fast-export  
RUN apk add --no-cache git mercurial python  
COPY /fast-export /home/fast-export  
RUN chmod +x /home/fast-export/*  
WORKDIR /home  
CMD ["/bin/sh"]

