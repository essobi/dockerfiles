FROM nachinius/php56-apache-nodejs  
  
MAINTAINER nachinius <ignacio.peixoto@gmail.com>  
  
#disable interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# install php mongodb extension  
RUN buildDeps="libssl-dev libsasl2-dev" \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& pecl install mongodb && pecl install mongo  
  
RUN echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongodb.ini  
RUN echo "extension=mongo.so" > $PHP_INI_DIR/conf.d/mongo.ini  
  

