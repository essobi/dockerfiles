FROM ubermuda/pandoc  
  
MAINTAINER Geoffrey Bachelet <geoffrey.bachelet@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV KINDLE_ARCHIVE kindlegen_linux_2.6_i386_v2_9.tar.gz  
  
RUN mkdir /kindle  
RUN apt-get install -y curl && \  
curl http://kindlegen.s3.amazonaws.com/$KINDLE_ARCHIVE | tar xzC /kindle && \  
apt-get remove -y curl

