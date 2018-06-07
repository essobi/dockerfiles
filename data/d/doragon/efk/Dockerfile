FROM centos:centos6  
  
MAINTAINER koide  
  
### common ###  
RUN yum -y update && \  
yum -y install java-1.7.0-openjdk curl-devel which unzip wget  
  
##### td-agent #####  
RUN yum -y --disableexcludes=main install gcc  
ADD ./conf/td-agent-install-redhat.sh /root/td-agent-install-redhat.sh  
RUN /bin/sh /root/td-agent-install-redhat.sh && \  
rm /root/td-agent-install-redhat.sh  
RUN rpm -ivh http://ftp.riken.jp/Linux/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
yum -y install geoip-devel --enablerepo=epel  
  
# Install plugins  
RUN /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-elasticsearch
&& \  
/usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-typecast && \  
/usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-map && \  
/usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-geoip && \  
/usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-rewrite-tag-filter  
  
# Setting files  
ADD ./conf/td-agent.conf /etc/td-agent/td-agent.conf  
  
### elasticsearch ###  
RUN rpm --import http://packages.elasticsearch.org/GPG-KEY-elasticsearch && \  
echo -e "[elasticsearch-1.3]\nname=Elasticsearch repository for 1.3.x
packages\nbaseurl=http://packages.elasticsearch.org/elasticsearch/1.3/centos\ngpgcheck=1\ngpgkey=http://packages.elasticsearch.org/GPG-
KEY-elasticsearch\nenabled=1" > /etc/yum.repos.d/elasticsearch.repo && \  
yum -y update  
RUN yum -y install elasticsearch  
RUN ln -s /etc/elasticsearch/ /usr/share/elasticsearch/config  
  
# Install Elasticsearch Plugins  
RUN /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head && \  
/usr/share/elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf && \  
/usr/share/elasticsearch/bin/plugin -install elasticsearch/marvel/latest && \  
/usr/share/elasticsearch/bin/plugin -install royrusso/elasticsearch-HQ && \  
/usr/share/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-
analysis-kuromoji/2.3.0  
  
# Setting files  
ADD ./conf/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
  
### kibana ###  
RUN wget http://download.elasticsearch.org/kibana/kibana/kibana-latest.zip &&
\  
unzip kibana-latest.zip && \  
mv kibana-latest /usr/local/kibana  
  
# Install Nginx  
RUN rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-
centos-6-0.el6.ngx.noarch.rpm && \  
yum -y update && \  
yum -y install nginx  
  
# Setting files  
ADD ./conf/kibana_config.js /usr/local/kibana/config.js  
ADD ./conf/nginx_default.conf /etc/nginx/conf.d/default.conf  
  
### common ###  
RUN yum -y clean all  
ADD ./conf/run.sh /root/run.sh  
  
# Expose ports.(td-agent, elasticsearch, kibana)  
EXPOSE 24220 24224  
EXPOSE 9200 9300  
EXPOSE 80  
# Define default command.  
CMD ["/bin/sh", "-c", "sh /root/run.sh; tail -f /dev/null"]  

