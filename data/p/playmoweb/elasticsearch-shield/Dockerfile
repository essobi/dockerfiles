FROM elasticsearch:2.2.0  
  
MAINTAINER steve@playmoweb.com  
  
RUN rm -rf /etc/elasticsearch  
RUN ln -s /usr/share/elasticsearch/config /etc/elasticsearch  
  
RUN /usr/share/elasticsearch/bin/plugin install license  
RUN /usr/share/elasticsearch/bin/plugin install shield  
  
#RUN /usr/share/elasticsearch/bin/shield/esusers useradd myuser -p mypassword
-r admin  

