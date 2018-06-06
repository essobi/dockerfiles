FROM alpine:3.6  
MAINTAINER Kouichi Machida <k-machida@aideo.co.jp>  
  
ENV MECAB_VERSION=0.996 \  
MECAB_DOWNLOAD_URL=https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
\  
MECAB_IPADIC_VERSION=2.7.0-20070801 \  
MECAB_IPADIC_DOWNLOAD_URL=https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM  
  
RUN apk add --update --no-cache --virtual .build-deps-mecab \  
boost-dev \  
file \  
g++ \  
git \  
make \  
openssl \  
perl \  
zlib-dev \  
\  
&& apk add --no-cache \  
bash \  
boost \  
curl \  
\  
&& curl -L -o /tmp/mecab.tar.gz "${MECAB_DOWNLOAD_URL}" \  
&& tar xzvf /tmp/mecab.tar.gz -C /tmp \  
&& cd /tmp/mecab-${MECAB_VERSION} \  
&& ./configure --prefix=/usr/local/ \--enable-utf8-only \  
&& make \  
&& make install \  
\  
&& curl -L -o /tmp/mecab-ipadic.tar.gz "${MECAB_IPADIC_DOWNLOAD_URL}" \  
&& tar xzvf /tmp/mecab-ipadic.tar.gz -C /tmp \  
&& cd /tmp/mecab-ipadic-${MECAB_IPADIC_VERSION} \  
&& ./configure --prefix=/usr/local/ \--with-charset=utf8 \  
&& make \  
&& make install \  
\  
&& cd /tmp \  
&& git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \  
&& cd mecab-ipadic-neologd \  
&& ./bin/install-mecab-ipadic-neologd -n -y \  
\  
&& apk del .build-deps-mecab \  
\  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
COPY ./entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

