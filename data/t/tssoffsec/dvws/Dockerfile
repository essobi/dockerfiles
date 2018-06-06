FROM tutum/lamp:latest  
  
MAINTAINER Christopher Dreher <christopher.dreher@daimler.com>  
  
  
RUN apt-get update && \  
apt-get install -y git curl  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
RUN chmod +x /usr/bin/composer  
  
WORKDIR /app  
RUN rm -fr /app  
RUN git clone https://github.com/interference-security/DVWS.git /app  
COPY conf/setup_dvws.sh /app  
RUN chmod +x /app/setup_dvws.sh && \  
/app/setup_dvws.sh  
  
# Clean-up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80 8080  
ONBUILD RUN cd /app && \  
composer update --no-interaction  
  
  
CMD ["/run.sh"]  

