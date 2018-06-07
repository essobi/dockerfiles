FROM openmonitoringproject/icinga2  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN yum -y install icinga2-ido-mysql mariadb wget \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& yum clean all  
  
ADD . /  
  
ENTRYPOINT ["/usr/local/bin/dockerize", "-template", "ido-
mysql.tmpl:/etc/icinga2/features-enabled/ido-mysql.conf"]  
CMD ["/entrypoint.sh"]  
  

