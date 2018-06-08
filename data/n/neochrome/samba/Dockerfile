# vim: ft=dockerfile  
FROM alpine:3.2  
MAINTAINER Johan Stenqvist <johan@stenqvist.net>  
LABEL Description="Simple Samba Shares"  
  
RUN apk --update add \  
curl \  
samba \  
&& curl -L https://github.com/neochrome/lsdvol/releases/download/v0.2.1/lsdvol
-o /bin/lsdvol \  
&& chmod +x /bin/lsdvol \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
COPY ./run.sh /  
EXPOSE 445  
CMD ./run.sh  

