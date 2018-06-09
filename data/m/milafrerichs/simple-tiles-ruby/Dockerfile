FROM ruby:2.2.0  
RUN apt-get update -qq \  
&& apt-get install -y build-essential libpq-dev \  
software-properties-common \  
libgdal-dev \  
libproj-dev \  
gdal-bin \  
libcairo2-dev \  
libpango1.0-dev  
  
ENV SIMPLE_TILES_VERSION 0.6.0  
  
RUN mkdir -p /usr/src/simple_tiles \  
&& curl -SL "https://github.com/propublica/simple-
tiles/archive/v$SIMPLE_TILES_VERSION.tar.gz" \  
| tar -xzC /usr/src/simple_tiles \  
&& cd "/usr/src/simple_tiles/simple-tiles-$SIMPLE_TILES_VERSION" \  
&& ./configure \  
&& make \  
&& make install  

