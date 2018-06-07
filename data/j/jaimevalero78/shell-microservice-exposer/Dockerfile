# Test  
FROM centos/httpd  
RUN useradd -s /bin/bash contint  
  
MAINTAINER Jaime Valero <jaimevalero78@yahoo.es>  
  
LABEL Description="Generic container to receives POST http request to a shell
script" Version="0.5"  
  
# Install packages  
RUN yum install -y mysql git wget && yum clean all -y  
  
RUN curl -L https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux32
> /usr/local/bin/jq && chmod +x /usr/local/bin/jq  
  
# Prepare environment  
RUN mkdir -p /tmp/scripts/shell-microservice-exposer  
ADD . /tmp/scripts/shell-microservice-exposer  
ADD _executor.sh /var/www/cgi-bin/  
  
RUN chmod -R 777 /tmp/ /var/www /var/log/httpd /etc/httpd/  
RUN chown -R apache:apache /var/www  
  
COPY etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf  
  
# Permissions  
RUN chmod +x -R /tmp/scripts/shell-microservice-exposer/  
  
# Apache  
#RUN sed -i 's/Options None/Options FollowSymLinks Indexes/g'
/etc/httpd/conf/httpd.conf  
#RUN httpd -T -k start #2>/dev/null 1>/dev/null  
#RUN ps -ef | grep httpd | grep -v grep  
RUN a=1  
  
USER apache  
  
ENTRYPOINT ["/tmp/scripts/shell-microservice-exposer/entrypoint.sh"]  
  
EXPOSE 8080  

