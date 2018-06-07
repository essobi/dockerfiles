FROM torvitas/php-fpm:5.6-root  
MAINTAINER "Sascha Marcel Schmidt" <docker@saschaschmidt.net>  
RUN apt-get update && apt-get install rsync openssh-client unzip -y && rm -r
/var/lib/apt/lists/*  
RUN bash -c "source /usr/local/etc/entrypoint.xdebug.functions.sh && \  
disableXDebug && \  
composer global remove codeception/codeception && \  
composer global update && \  
composer global require --dev deployer/deployer:~3.0 deployphp/recipes:~3.0 &&
\  
enableXDebug"  
COPY bin/ /usr/local/bin/  
CMD ["dep:develop"]  

