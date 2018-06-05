FROM buildpack-deps:jessie  
  
  
ENV PROTOBUF_VERSION 3.3.0  
ENV PROTOBUF_DOWNLOAD_URL
https://github.com/google/protobuf/archive/v3.3.0.tar.gz  
ENV PROTOBUF_DOWNLOAD_SHA256
94c414775f275d876e5e0e4a276527d155ab2d0da45eed6b7734301c330be36e  
  
  
RUN set -ex \  
\  
&& buildDeps=' \  
unzip \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O protobuf.tar.gz "${PROTOBUF_DOWNLOAD_URL}" \  
&& echo "${PROTOBUF_DOWNLOAD_SHA256} *protobuf.tar.gz" | sha256sum -c - \  
\  
&& mkdir -p /usr/src/protobuf \  
&& tar -xzf protobuf.tar.gz -C /usr/src/protobuf --strip-components=1 \  
&& rm protobuf.tar.gz \  
\  
&& cd /usr/src/protobuf \  
\  
&& ./autogen.sh \  
&& ./configure \  
&& make check \  
&& make \  
&& make install \  
&& ldconfig \  
&& protoc \--version \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
&& cd / \  
&& rm -r /usr/src/protobuf  
  
  
CMD ["protoc"]  

