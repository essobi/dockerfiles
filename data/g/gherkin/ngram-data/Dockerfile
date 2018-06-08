FROM frolvlad/alpine-oraclejdk8:slim  
  
MAINTAINER think@hotmail.de  
  
ENV NGRAMS_VERSION=20150817  
RUN apk --update add curl ca-certificates openssl libarchive-tools \  
&& mkdir /ngrams \  
&& curl https://languagetool.org/download/ngram-data/ngrams-
en-${NGRAMS_VERSION}.zip \  
| bsdtar -xf- -C /ngrams  

