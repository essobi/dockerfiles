FROM webdevops/samson-deployment  
  
MAINTAINER contact@sponk.pl  
  
RUN apt-get update  
RUN apt-get -y install git subversion make g++ python curl php5-dev chrpath &&
apt-get clean  
  
# depot tools  
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
/usr/local/depot_tools  
ENV PATH $PATH:/usr/local/depot_tools  
ENV NO_INTERACTION 1  
  
# download v8  
RUN cd /tmp && fetch v8 && \  
export GYPFLAGS="-Dv8_use_external_startup_data=0" && \  
export GYPFLAGS="${GYPFLAGS} -Dlinux_use_bundled_gold=0" && \  
# compile v8  
cd /tmp/v8 && make native library=shared snapshot=on -j8 && \  
  
# Install to /usr  
sudo mkdir -p /usr/local/lib /usr/local/include && \  
cd /tmp/v8 && cp out/native/lib.target/lib*.so /usr/local/lib/ && \  
cd /tmp/v8 && cp -R include/* /usr/local/include && \  
  
# Fix libv8.so's RUNPATH header  
sudo chrpath -r '$ORIGIN' /usr/local/lib/libv8.so && \  
  
# Install libv8_libplatform.a (V8 >= 5.2.51)  
sudo echo -e "create /usr/local/lib/libv8_libplatform.a\naddlib
/tmp/v8/out/native/obj.target/src/libv8_libplatform.a\nsave\nend" | sudo ar -M
&& \  
  
# get v8js, compile and install  
git clone https://github.com/phpv8/v8js.git /tmp/v8js && cd /tmp/v8js && git
checkout master && \  
  
#RUN cp /tmp/v8/out/native/snapshot_blob.bin /usr/local/lib/ && \  
# cp /tmp/v8/out/native/natives_blob.bin /usr/local/lib/ && \  
cd /tmp/v8js && phpize && ./configure \--with-v8js=/usr/local && \  
sudo make && sudo make install && echo extension=v8js.so >
/etc/php5/cli/conf.d/99-v8js.ini && \  
rm -Rdf /tmp/v8/* && rm -Rdf /tmp/v8js/*  

