FROM mehrdadkhah/lemp-php7-full:ffmpeg  
  
MAINTAINER Mehrdad Dadkhah <mehrdad@dadkhah.me>  
  
# install and active newrelic  
COPY ./newrelicRun.sh /newrelicRun.sh  
RUN chmod +x /newrelicRun.sh  
  
# Install New Relic daemon  
RUN apt-get update && \  
apt-get -yq install wget && \  
wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list  
  
RUN apt-get update && \  
apt-get -yq install newrelic-php5  
  
# Modify the default entrypoint to call our new run script at its end  
RUN /newrelicRun.sh  
  
# Setup environment variables for initializing New Relic  
COPY ./newrelic.ini /usr/local/etc/php/conf.d/newrelic.ini  
  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80 443  

