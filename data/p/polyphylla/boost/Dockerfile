FROM alpine:latest  
  
MAINTAINER Wang Qun, <qun.wang@live.cn>  
  
RUN \  
apk add --no-cache --virtual .build-deps g++ make curl linux-headers python-
dev \  
&& curl -SL
"http://downloads.sourceforge.net/project/boost/boost/1.62.0/boost_1_62_0.tar.bz2?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fboost%2Ffiles%2Fboost%2F1.62.0%2F&ts=$(date
+%s)&use_mirror=superb-sea2" \  
-o boost_1_62_0.tar.bz2 \  
&& [ $(sha1sum boost_1_62_0.tar.bz2 | awk '{print $1}') ==
'5fd97433c3f859d8cbab1eaed4156d3068ae3648' ] \  
&& tar --bzip2 -xf boost_1_62_0.tar.bz2 \  
&& cd boost_1_62_0 \  
&& ./bootstrap.sh --prefix=/usr/local \  
&& ./b2 -a -sHAVE_ICU=1 \  
&& ./b2 install \  
&& cd .. \  
&& rm -rf boost_1_62_0.tar.bz2 boost_1_62_0  

