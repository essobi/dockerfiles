################################################################################  
# Base image  
################################################################################  
  
FROM marmelab/composer-hhvm:latest  
MAINTAINER Billy Nguyen <billy.nguyen@noria.no>  
  
  
################################################################################  
# Build instructions  
################################################################################  
  
ENV HOME /root  
# Register the COMPOSER_HOME environment variable  
ENV COMPOSER_HOME /composer  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
RUN apt-get update -y && apt-get install -y software-properties-common \  
&& add-apt-repository "deb http://dl.hhvm.com/ubuntu trusty main" \  
&& apt-add-repository ppa:git-core/ppa \  
&& apt-get update -y \  
&& apt-get install -y hhvm git curl \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo "date.timezone = UTC" >> /etc/hhvm/php.ini \  
&& composer self-update && composer global require "contemi/pegasus-composer-
installer:1.*"  
  
ENTRYPOINT ["composer", "--ansi"]

