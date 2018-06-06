FROM richarvey/nginx-php-fpm:php71  
MAINTAINER Sam Mousa <sam@mousa.nl>  
  
RUN apk --update add build-base  
  
# Install sassc  
RUN cd /tmp && \  
git clone https://github.com/sass/libsass.git && \  
export SASS_LIBSASS_PATH=/tmp/libsass && \  
git clone https://github.com/sass/sass-spec.git && \  
export SASS_SPEC_PATH=/tmp/sass-spec && \  
git clone https://github.com/sass/sassc.git && \  
cd libsass && \  
make && \  
cd .. && \  
cd sassc && \  
script/bootstrap && \  
make && \  
mv bin/sassc /bin/sassc && \  
rm -rf /tmp/*  

