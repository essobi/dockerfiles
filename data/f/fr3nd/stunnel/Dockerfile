FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
libssl-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV STUNNEL_VERSION 5.10  
WORKDIR /usr/src  
RUN curl -L
https://www.stunnel.org/downloads/stunnel-${STUNNEL_VERSION}.tar.gz | tar xvz  
WORKDIR /usr/src/stunnel-${STUNNEL_VERSION}  
RUN ./configure --prefix=/usr && make && make install  
  
WORKDIR /  
  
ENTRYPOINT [ "/usr/bin/stunnel" ]  

