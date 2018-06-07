FROM golang  
  
RUN mkdir /jobs  
  
RUN addgroup --gid 1000 jobber_client  
RUN useradd -u 1000 -g jobber_client --home /jobs jobber_client  
  
RUN go get github.com/dshearer/jobber \  
&& cd src/github.com/dshearer/jobber \  
&& git checkout v1.0.3 \  
&& make  
  
WORKDIR /jobs  
  
RUN apt-get update && apt-get install -y --no-install-recommends php5-cli
php5-mysql php5-gd php5-mcrypt php5-redis mysql-client  
  
ENV COMPOSER_VERSION master  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN composer global require drush/drush:dev-master  
  
ENV PATH "/root/.composer/vendor/bin:$PATH"  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile  
ENTRYPOINT []  
  
CMD ["jobberd"]

