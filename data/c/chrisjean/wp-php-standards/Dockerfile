FROM php  
MAINTAINER Chris Jean <chris@chrisjean.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "date.timezone = UTC" >> /usr/local/etc/php/php.ini  
RUN echo "memory_limit = -1" >> /usr/local/etc/php/php.ini  
RUN echo "phar.readonly = 0" >> /usr/local/etc/php/php.ini  
  
RUN pear install PHP_CodeSniffer  
RUN git clone https://github.com/WordPress-Coding-Standards/WordPress-Coding-
Standards.git /usr/local/lib/php/PHP/CodeSniffer/Standards/WordPress  
RUN phpcs --config-set installed_paths
/usr/local/lib/php/PHP/CodeSniffer/Standards/WordPress  
  
RUN mkdir /project  
VOLUME ["/project"]  
WORKDIR "/project"  
  
CMD phpcs --standard=WordPress .  

