FROM michaeltigr/zebra-php-base:latest  
  
LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"  
  
USER root  
  
# Set the Drush version.  
ENV DRUSH_VERSION 8.1.13  
# Install Drush 8 with the phar file.  
RUN curl -fsSL -o /usr/local/bin/drush "https://github.com/drush-
ops/drush/releases/download/$DRUSH_VERSION/drush.phar" && \  
chmod +x /usr/local/bin/drush  
  
# Test your install.  
RUN drush core-status  
  
# Install Java, druflow & assemble gradle & groovy.  
ENV JAVA_HOME=/usr  
RUN apk add --update --no-cache openjdk7-jre-base \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone -b master https://github.com/michael-molchanov/druflow.git \  
&& cd druflow \  
&& ./gradlew assemble  

