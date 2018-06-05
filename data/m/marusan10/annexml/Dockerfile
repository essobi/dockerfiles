FROM alpine  
  
RUN apk add --update --no-cache --virtual=.annexml-deps \  
bash \  
sed \  
curl \  
python \  
libgcc \  
libstdc++ \  
libgomp \  
libatomic \  
&& apk add --update --no-cache --virtual=.annexml-build-deps \  
make \  
g++ \  
&& mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& curl -SLO https://github.com/yahoojapan/AnnexML/archive/master.tar.gz \  
&& tar zxvf master.tar.gz \  
&& rm master.tar.gz \  
&& cd AnnexML-master \  
&& sed -i 's/^CXXFLAG += -DUSEFMA -mfma/#\0/g' src/Makefile \  
&& make -C src/ annexml \  
&& ln -s /usr/local/src/AnnexML-master/src/annexml /usr/local/bin/annexml \  
&& apk del .annexml-build-deps  
  

