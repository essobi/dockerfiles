FROM torvitas/php-fpm:5.6  
MAINTAINER "Sascha Marcel Schmidt" <docker@saschaschmidt.net>  
  
ARG DEPLOYER_VERSION=4.0.0  
ARG DEPLOYPHP_RECIPES_VERSION=dev-master  
  
RUN apt-get update && apt-get install rsync openssh-client unzip -y && rm -r
/var/lib/apt/lists/*  
RUN composer global remove codeception/codeception && \  
composer global update && \  
composer global require --dev "deployer/deployer:${DEPLOYER_VERSION}"
"deployphp/recipes:$DEPLOYPHP_RECIPES_VERSION"  
COPY bin/ /usr/local/bin/  
CMD ["dep"]  

