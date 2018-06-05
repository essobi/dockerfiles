FROM alpine:edge  
MAINTAINER Peter Mutsaers <plmuon@gmail.com>  
  
RUN apk add --no-cache openssh borgbackup tini  
COPY run.sh /  
  
EXPOSE 22  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/run.sh"]  

