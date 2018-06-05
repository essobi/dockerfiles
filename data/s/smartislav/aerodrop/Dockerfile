FROM debian:wheezy  
  
RUN apt-get update \  
&& apt-get install -y curl ca-certificates apt-transport-https \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
RUN echo 'deb https://deb.nodesource.com/node_0.10 wheezy main' >
/etc/apt/sources.list.d/nodesource.list  
  
RUN apt-get update \  
&& apt-get install -y mercurial bison make curl wget binutils gcc python-
software-properties build-essential git acl --no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir server  
COPY build.sh /server/build.sh  
EXPOSE 11211  
RUN /server/build.sh  
  

