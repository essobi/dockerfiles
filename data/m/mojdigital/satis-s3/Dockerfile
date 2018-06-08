FROM iainmckay/satis-s3  
  
# Update composer and satis to the latest versions  
RUN docker-php-ext-install mbstring && \  
php composer.phar self-update && \  
rm -rf /satis && \  
php composer.phar create-project composer/satis --stability=dev --no-
interaction  
  
# Overwrite existing run.sh with our own version.  
# Our version additionally configures GitHub auth for composer to avoid API
usage limits,  
# and uses different command line options for syncing files to S3.  
ADD run.sh /run.sh  

