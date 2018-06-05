# https://hub.docker.com/_/ruby/  
FROM ruby:2.4  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH
/usr/local/ruby/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN apt-get update \  
&& apt-get install -y -q wget \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install --global yarn  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

