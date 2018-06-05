FROM phpearth/php:7.1-apache  
  
MAINTAINER Ádám Liszkai <adaliszk@gmail.com>  
  
ARG RUN_TYPE=default  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/adaliszk/bechmark-php-cli.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="0.1.0" \  
org.label-schema.vendor="adaliszk" \  
org.label-schema.name="bechmark-php-cli" \  
org.label-schema.description="Simple tester to check different php versions
and installed modules how's effect the script runtimes" \  
org.label-schema.url="https://github.com/adaliszk/bechmark-php-cli.git"  
# Add project files  
ADD . /srv  
  
# Configure Apache2 VHOST  
ADD ./vhost.conf /etc/apache2/sites-enabled/default  
  
# Expose HTTP port  
EXPOSE 80  
  
# Run the default CMD  
CMD ["/sbin/runit-wrapper"]

