FROM kitpages/fizen-web  
MAINTAINER Kibatic <system@kibatic.com>  
  
RUN apt-get -qqq update && DEBIAN_FRONTEND=noninteractive apt-get install -qqq
-y \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -O - https://packagecloud.io/gpg.key | apt-key add -  
RUN echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list  
  
RUN apt-get -qqq update && DEBIAN_FRONTEND=noninteractive apt-get install -qqq
-y \  
blackfire-php && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
/etc/php5/fpm/conf.d/blackfire.ini  

