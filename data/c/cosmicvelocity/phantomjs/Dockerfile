FROM debian:stretch-slim  
MAINTAINER Kouichi Machida <k-machida@aideo.co.jp>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
LANGUAGE=en_US \  
LC_ALL=C \  
LANG=en_US.UTF-8  
ENV PHANTOM_JS_VERSION 2.1.1  
ENV
PHANTOM_JS_URL=https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_JS_VERSION}-linux-x86_64.tar.bz2
\  
PHANTOM_JS_DOWNLOAD_SHA256=86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f  
  
RUN apt-get update \  
&& apt-get upgrade \  
&& apt-get install -y --no-install-recommends \  
bzip2 \  
ca-certificates \  
curl \  
fontconfig \  
fonts-takao-gothic \  
fonts-takao-mincho \  
\  
&& curl -L -o /tmp/phantomjs.tar.bz2 "${PHANTOM_JS_URL}" \  
&& echo "${PHANTOM_JS_DOWNLOAD_SHA256} */tmp/phantomjs.tar.bz2" | sha256sum -c
- \  
&& mkdir -p /tmp/phantomjs \  
&& tar -xf /tmp/phantomjs.tar.bz2 -C /tmp/phantomjs --strip-components=1 \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \  
&& mv /tmp/phantomjs/README.md / \  
&& mv /tmp/phantomjs/LICENSE.BSD / \  
&& mv /tmp/phantomjs/third-party.txt / \  
\  
&& apt-get purge -y \  
bzip2 \  
curl \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get clean -y \  
\  
&& rm -rf /tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/local/bin/phantomjs"]  

