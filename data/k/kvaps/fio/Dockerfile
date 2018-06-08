FROM ubuntu  
  
RUN apt-get -y update \  
&& apt-get -y install libaio-dev curl gcc make zlib1g-dev \  
&& curl -L https://github.com/axboe/fio/archive/fio-3.5.tar.gz | tar xzf - \  
&& cd fio-* \  
&& ./configure \  
&& make \  
&& make install \  
&& cd \- \  
&& rm -rf fio-* \  
&& apt-get clean  
  
ENTRYPOINT [ "/usr/local/bin/fio" ]  

