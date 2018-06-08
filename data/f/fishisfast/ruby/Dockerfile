FROM ruby:2.3  
ENV PACKAGES imagemagick \  
ghostscript \  
libzbar-dev \  
zbar-tools \  
unzip \  
pgdbf \  
postgresql-client \  
nodejs \  
npm \  
nodejs-legacy \  
pdftk  
  
RUN echo 'gem: --no-ri --no-rdoc' > ~/.gemrc  
  
RUN apt-get update && apt-get install -y $PACKAGES \  
&& apt-get autoremove && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV BUNDLE_PATH /bundle  
ENV BUNDLE_WITHOUT development:test  
RUN mkdir -p $BUNDLE_PATH  

