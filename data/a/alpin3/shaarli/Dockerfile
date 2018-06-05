FROM alpin3/php-apache  
MAINTAINER kost - https://github.com/kost  
  
ENV SHAARLI_VERSION=0.8.0 \  
SHAARLI_PKG=shaarli.tgz  
  
RUN apk --update --no-cache add wget ca-certificates php5-zlib php5-dom \  
&& mkdir /php \  
&& cd /php \  
&& wget -O /tmp/$SHAARLI_PKG
https://github.com/shaarli/Shaarli/archive/v$SHAARLI_VERSION.tar.gz \  
&& tar xvzf /tmp/$SHAARLI_PKG \  
&& cd Shaarli* \  
&& mv * .. \  
&& cd .. \  
&& composer update --no-dev \  
&& chown -R apache:apache cache data pagecache tmp \  
&& echo "Success"  
ADD scripts/ /scripts  
VOLUME ["/php/data"]  
  

