FROM alpine  
MAINTAINER Toby Corkindale <tjc@github.com>  
EXPOSE 3690  
CMD ["/usr/bin/svnserve", "-r", "/svn", "-d", "--foreground"]  
  
RUN mkdir -p /svn && apk update && apk add subversion  
RUN svnadmin create /svn/repo  
ADD svnserve.conf /svn/repo/conf/svnserve.conf  
  
VOLUME /svn  

