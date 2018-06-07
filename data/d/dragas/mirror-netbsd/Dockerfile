FROM alpine:3.7  
MAINTAINER Stefano Marinelli <stefano@dragas.it>  
  
RUN apk --no-cache add wget cvs openssh; mkdir /root/.ssh  
  
ADD known_hosts /root/.ssh/  
  
ENTRYPOINT cd /toupdate/; CVS_RSH=ssh;
CVSROOT=anoncvs@anoncvs.NetBSD.org:/cvsroot; cvs update -dP && wget -B
http://www.NetBSD.org/ -nv -xnH -N -Fi mirrors/fetch.html  

