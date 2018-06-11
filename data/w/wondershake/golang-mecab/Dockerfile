FROM golang:1.9.2-alpine3.7  
LABEL maintainer="Wondershake"  
  
ENV mecab_url
https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE  
ENV ipadic_url
https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM  
ENV neologd_rev 6e90aadbe26c3f7a8f829d422465a7cbad603258  
ENV build_deps "curl git bash file sudo openssh gcc g++ make"  
ENV runtime_deps "openssl musl-dev libstdc++"  
  
WORKDIR /root  
  
RUN apk add --no-cache -t .build_deps ${build_deps} \  
&& apk add --no-cache ${runtime_deps} \  
# Install MeCab  
&& curl -LSfs -o mecab.tar.gz ${mecab_url} \  
&& tar zxf mecab.tar.gz \  
&& rm -f mecab.tar.gz \  
&& cd $(ls | grep mecab) \  
&& ./configure --enable-utf8-only --with-charset=utf8 \  
&& make \  
&& make install \  
&& cd \  
&& rm -rf mecab* \  
# Install IPADic  
&& curl -LSfs -o mecab-ipadic.tar.gz ${ipadic_url} \  
&& tar zxf mecab-ipadic.tar.gz \  
&& rm -r mecab-ipadic.tar.gz \  
&& cd $(ls | grep mecab-ipadic) \  
&& ./configure --with-charset=utf8 \  
&& make \  
&& make install \  
&& cd \  
&& rm -rf mecab-ipadic* \  
# Install NEologd  
&& git clone https://github.com/neologd/mecab-ipadic-neologd.git \  
&& cd mecab-ipadic-neologd \  
&& git reset --hard ${neologd_rev} \  
&& bin/install-mecab-ipadic-neologd -n -y \  
&& cd \  
&& rm -rf mecab-ipadic-neologd  
  
ENV CGO_LDFLAGS "-L/usr/local/lib -lmecab -lstdc++"  
ENV CGO_CFLAGS "-I/usr/local/include"  
# Delete .build_deps packages in production  
# RUN apk del .build_deps  

