FROM ubuntu:14.04  
MAINTAINER Chris Antenesse <chris@antenesse.net>  
RUN apt-get -qq update  
RUN apt-get -y install curl git mercurial  
RUN curl -L http://golang.org/dl/go1.3.linux-amd64.tar.gz |tar zx -C
/usr/local  
CMD ["--help"]  
ENTRYPOINT ["/usr/local/go/bin/go"]

