FROM python:2.7  
  
WORKDIR /src  
  
ENV TABLEAU_SDK_VERSION 10-3-3  
  
RUN set -ex \  
&& wget -O SDK.tar.gz "https://downloads.tableau.com/tssoftware/Tableau-SDK-
Python-Linux-64Bit-${TABLEAU_SDK_VERSION}.tar.gz" \  
&& mkdir -p /sdk \  
&& tar -xzf SDK.tar.gz -C /sdk --strip-components=1 \  
&& rm SDK.tar.gz \  
&& cd /sdk \  
&& python setup.py install \  
&& rm -rf /sdk \  
&& apt-get clean  
  
ENV TABLEAU_SDK_DIR /usr/local/lib/python2.7/site-packages/tableausdk  
ENV LIB_DIR /usr/lib/x86_64-linux-gnu  
  
RUN set -ex \  
\  
&& echo "Installing missing dep libpcre16.so.0" \  
&& echo "deb http://deb.debian.org/debian testing main" >
/etc/apt/sources.list.d/testing.list \  
&& apt-get update \  
&& apt-get -t testing install libpcre16-3 \  
&& ln -s $LIB_DIR/libpcre16.so.3 /usr/lib/libpcre16.so.0 \  
&& apt-get clean \  
\  
&& echo "Replacing broken libcurl lib" \  
&& ln -sf $LIB_DIR/libcurl.so $TABLEAU_SDK_DIR/lib/libcurl.so \  
&& ln -sf $LIB_DIR/libcurl.so.4 $TABLEAU_SDK_DIR/lib/libcurl.so.4 \  
&& rm $TABLEAU_SDK_DIR/lib/libcurl.so.4.4.0  

