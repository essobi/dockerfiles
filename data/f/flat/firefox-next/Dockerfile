FROM debian:testing  
LABEL maintainer "Vincent Giersch <vincent+docker@flat.io>"  
# Install Firefox  
RUN echo 'deb http://http.debian.net/debian experimental main' >
/etc/apt/sources.list.d/firefox.list \  
&& apt-get update \  
&& apt-get install -y -t experimental firefox --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install node / git / ssh  
ENV NODE_VERSION 8.11.2  
RUN apt-get update \  
&& apt-get install -y wget ca-certificates xz-utils git ssh --no-install-
recommends \  
&& wget --no-verbose -O /tmp/node.tar.xz
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz"
\  
&& tar -xJf /tmp/node.tar.xz -C /usr/local --strip-components=1 \--no-same-
owner \  
&& apt-get purge -y xz-utils wget \  
&& rm -rf /var/lib/apt/lists/* /tmp/node.tar.xz \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN groupadd -g 999 user && \  
useradd -m -d /home/user -r -u 999 -g user user  
USER user  

