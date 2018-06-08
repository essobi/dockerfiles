FROM jenkins  
  
USER root  
  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq sudo ant php5-cli
php5-mysql php5-gd php5-intl php5-curl php5-xcache \  
&& rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt/*  
  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
RUN sed -i 's/xcache.size = 60M/xcache.size = 0/' /etc/php5/mods-
available/xcache.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer && chown jenkins /usr/bin/composer  
  
USER jenkins  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF-8  

