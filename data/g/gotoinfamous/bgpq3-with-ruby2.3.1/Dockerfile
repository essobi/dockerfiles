FROM ruby:2.3.1  
WORKDIR /tmp  
  
RUN apt-get update  
  
RUN wget https://github.com/snar/bgpq3/archive/v0.1.35-rc.tar.gz \  
&& tar -xf v0.1.35-rc.tar.gz \  
&& cd bgpq3-0.1.35-rc \  
&& ./configure \  
&& make \  
&& make install \

