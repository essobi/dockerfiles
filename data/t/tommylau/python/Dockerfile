FROM python:2-slim  
  
RUN buildDeps=" \  
libssl-dev \  
gcc \  
swig \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/include/x86_64-linux-gnu/openssl/opensslconf.h
/usr/include/openssl/opensslconf.h \  
&& easy_install M2Crypto \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get autoremove -y  

