FROM alpine  
  
ENV _3PROXY_VERSION 0.8.7  
ENV _3PROXY_DOWNLOAD_URL
https://codeload.github.com/z3APA3A/3proxy/tar.gz/3proxy-0.8.7  
ENV _3PROXY_DOWNLOAD_SHA1 d69a371db05f0c8438402192aec6c09c5f69a999  
  
RUN set -ex \  
\  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
linux-headers \  
make \  
musl-dev \  
tar \  
openssl \  
\  
&& wget -O 3proxy.tar.gz "$_3PROXY_DOWNLOAD_URL" \  
&& echo "$_3PROXY_DOWNLOAD_SHA1 *3proxy.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src/3proxy \  
&& tar -xzf 3proxy.tar.gz -C /usr/src/3proxy --strip-components=1 \  
&& rm 3proxy.tar.gz \  
\  
&& make -C /usr/src/3proxy -f Makefile.Linux \  
&& make -C /usr/src/3proxy -f Makefile.Linux install \  
\  
&& rm -r /usr/src/3proxy \  
\  
&& apk del .build-deps  
  
COPY 3proxy.cfg /etc  
EXPOSE 8080  
ENTRYPOINT ["3proxy", "/etc/3proxy.cfg"]  

