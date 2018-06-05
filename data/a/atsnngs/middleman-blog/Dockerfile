FROM ruby:2.5.1-alpine3.7  
MAINTAINER Atsushi Nagase<a@ngs.io>  
  
ENV MECAB_VERSION 0.996  
ENV IPADIC_VERSION 2.7.0-20070801  
ENV mecab_url
https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE  
ENV ipadic_url
https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM  
ENV build_deps 'file sudo'  
ENV dependencies 'openssl sqlite-dev build-base git curl git bash python
nodejs nodejs-npm openssh perl imagemagick'  
  
RUN apk add --update \--no-cache ${build_deps} \  
# Install dependencies  
&& apk add --update \--no-cache ${dependencies} \  
# Install MeCab  
&& curl -SL -o mecab-${MECAB_VERSION}.tar.gz ${mecab_url} \  
&& tar zxf mecab-${MECAB_VERSION}.tar.gz \  
&& cd mecab-${MECAB_VERSION} \  
&& ./configure --enable-utf8-only --with-charset=utf8 \  
&& make \  
&& make install \  
&& cd \  
# Install IPA dic  
&& curl -SL -o mecab-ipadic-${IPADIC_VERSION}.tar.gz ${ipadic_url} \  
&& tar zxf mecab-ipadic-${IPADIC_VERSION}.tar.gz \  
&& cd mecab-ipadic-${IPADIC_VERSION} \  
&& ./configure --with-charset=utf8 \  
&& make \  
&& make install \  
&& cd \  
# Install Neologd  
&& git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \  
&& mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y \  
# Clean up  
&& apk del ${build_deps} \  
&& rm -rf \  
mecab-${MECAB_VERSION}* \  
mecab-${IPADIC_VERSION}* \  
mecab-ipadic-neologd  
  
RUN mkdir tagger && cd tagger && \  
curl -o tree-tagger-linux-3.2.tar.gz http://www.cis.uni-
muenchen.de/~schmid/tools/TreeTagger/data/tree-tagger-linux-3.2.tar.gz && \  
curl -o tagger-scripts.tar.gz http://www.cis.uni-
muenchen.de/~schmid/tools/TreeTagger/data/tagger-scripts.tar.gz && \  
curl -o install-tagger.sh http://www.cis.uni-
muenchen.de/~schmid/tools/TreeTagger/data/install-tagger.sh && \  
curl -o english-par-linux-3.2.bin.gz http://www.cis.uni-
muenchen.de/~schmid/tools/TreeTagger/data/english-par-linux-3.2.bin.gz && \  
/bin/sh install-tagger.sh && \  
rm -f *.tar.gz && \  
ln -s $(pwd)/cmd/* /usr/bin && \  
ln -s $(pwd)/cmd/tree-tagger-english $(pwd)/bin/tree-tagger  
  
ENTRYPOINT ["/bin/bash"]  

