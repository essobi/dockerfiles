FROM kawanamiyuu/docker-centos-supervisord  
  
# install httpd  
RUN yum install -y httpd  
RUN echo '[program:httpd]' >> /etc/supervisord.conf  
RUN echo 'command=service httpd start' >> /etc/supervisord.conf  
  
# install java  
RUN yum install -y java-1.7.0-openjdk  
  
# install Elasticsearch  
RUN wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.4.noarch.rpm  
RUN rpm -ivh elasticsearch-1.3.4.noarch.rpm  
RUN echo '[program:elasticsearch]' >> /etc/supervisord.conf  
RUN echo 'command=service elasticsearch start' >> /etc/supervisord.conf  
  
# add Elasticsearch Index Template  
# http://qiita.com/harukasan/items/4ec517d8d96f557367e1  
RUN mkdir /etc/elasticsearch/templates/  
ADD dynamic_template.json /etc/elasticsearch/templates/  
  
# install fluentd  
RUN curl -L http://toolbelt.treasuredata.com/sh/install-redhat.sh | bash  
RUN mv -f /etc/td-agent/td-agent.conf /etc/td-agent/td-agent.conf.org  
ADD td-agent.conf /etc/td-agent/  
RUN echo '[program:td-agent]' >> /etc/supervisord.conf  
RUN echo 'command=service td-agent start' >> /etc/supervisord.conf  
  
# install fluent-plugin-elasticsearch  
RUN yum install -y libcurl-devel  
RUN /usr/lib64/fluent/ruby/bin/gem install fluent-plugin-elasticsearch  
  
# install Kibana  
RUN wget https://download.elasticsearch.org/kibana/kibana/kibana-3.1.1.tar.gz
-O /opt/kibana-3.1.1.tar.gz  
RUN tar xzvf /opt/kibana-3.1.1.tar.gz -C /opt/  
RUN rm -rf /var/www/html  
RUN ln -s /opt/kibana-3.1.1 /var/www/html  
  
# sshd  
EXPOSE 22  
# httpd  
EXPOSE 80  
# Elasticsearch  
EXPOSE 9200  
# fluentd  
EXPOSE 24224  

