FROM debian:wheezy  
MAINTAINER Vincenzo Petrucci (nahime)  
ENV DEBIAN_FRONTEND noninteractive  
ADD dotdeb.gpg /etc/apt/dotdeb.gpg  
RUN apt-key add /etc/apt/dotdeb.gpg && \  
echo "deb http://packages.dotdeb.org wheezy all" >
/etc/apt/sources.list.d/dotdeb.list && \  
echo "deb http://packages.dotdeb.org wheezy-php55 all" >>
/etc/apt/sources.list.d/dotdeb.list  
CMD true  

