FROM alpine  
MAINTAINER Walker Lee <walkerlee.tw@gmail.com>  
  
RUN apk -U --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/community/
add tini subversion \  
&& rm -rf /var/cache/apk/*  
  
VOLUME ["/var/svn/"]  
  
EXPOSE 3690  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
CMD ["svnserve", "-d", "-r", "/var/svn/", "--log-file", "/dev/stdout", "--
foreground"]  

