FROM python:3.5  
  
RUN set -ex \  
&& buildDeps=' \  
build-essential \  
cmake \  
libjson-c-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& echo 'deb http://deb.debian.org/debian sid main' > /etc/apt/sources.list \  
&& apt-get update -y && apt-get install -y swig3.0 && ln -s /usr/bin/swig3.0
/usr/bin/swig && rm -rf /var/lib/apt/lists/*  
  
RUN wget -O mraa.tar.gz https://github.com/intel-iot-
devkit/mraa/archive/v1.5.1.tar.gz \  
&& wget -O upm.tar.gz https://github.com/intel-iot-
devkit/upm/archive/08a46ee8e64dab0eb8c5145ec1c1fe8d5f20821b.tar.gz \  
&& mkdir -p /usr/src/mraa /usr/src/upm \  
&& tar -xzC /usr/src/mraa --strip-components=1 -f mraa.tar.gz \  
&& tar -xzC /usr/src/upm --strip-components=1 -f upm.tar.gz \  
&& rm upm.tar.gz mraa.tar.gz  
  
RUN cd /usr/src/mraa \  
&& cmake . -DBUILDARCH="MOCK" -DBUILDSWIGNODE=OFF && make -j$(nproc) \  
&& make install && ldconfig  
  
RUN cd /usr/src/upm \  
&& cmake . -DBUILDSWIGPYTHON=ON -DBUILDEXAMPLES=OFF -DBUILDSWIGNODE=OFF
-DBUILDSWIGJAVA=OFF \  
&& make -j$(nproc) \  
&& make install && ldconfig \  
&& rm -rf /usr/src/upm /usr/src/mraa

