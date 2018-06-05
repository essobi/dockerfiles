# Version: 0.0.1  
FROM debian:jessie-backports  
MAINTAINER Oleg Vyukov <gelo@vyukov.ru>  
  
  
RUN echo "deb http://httpredir.debian.org/debian/ jessie-backports main
contrib non-free" > /etc/apt/sources.list.d/backports.list && \  
echo "deb http://httpredir.debian.org/debian/ jessie main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb http://httpredir.debian.org/debian/ jessie-updates main contrib non-
free" >> /etc/apt/sources.list &&\  
echo "deb http://security.debian.org jessie/updates main contrib non-free" >>
/etc/apt/sources.list  
  
# maven и openjdk 8  
RUN apt-get update && apt-get install -t jessie-backports -y \  
ansible \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD vyukov.ru.CA.crt /usr/local/share/ca-certificates/vyukov.CA.crt  
RUN update-ca-certificates

