FROM centos:6  
MAINTAINER nattapon <lordhackalot@gmail.com>  
  
#RUN rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
#RUN sed -i -e "s|^;date.timezone =.*$|date.timezone = Asia/Bangkok|"
/etc/php.ini  
#RUN rpm -i http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-
release-1.0-11.ius.centos6.noarch.rpm  
ENV root_tmp /root/tmp  
ENV fileshared 52.74.40.153  
RUN curl -o /etc/yum.repos.d/elasticsearch.repo -sSL
http://${fileshared}/elasticsearch/elasticsearch.repo  
RUN mkdir -p $root_tmp && curl -o ${root_tmp}/elasticsearch.sysconfig -SL
http://${fileshared}/elasticsearch/elasticsearch.sysconfig  
RUN curl -o ${root_tmp}/elasticsearch.yml -SL
http://${fileshared}/elasticsearch/elasticsearch.yml  
RUN curl -o ${root_tmp}/run.sh -SL http://${fileshared}/elasticsearch/run.sh  
  
RUN rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y which sudo tar lsof gcc libcurl-devel java-1.7.0-openjdk
java-1.7.0-openjdk-devel elasticsearch  
RUN sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
RUN ulimit -n 65536  
RUN cp ${root_tmp}/elasticsearch.sysconfig /etc/sysconfig/elasticsearch && cp
-f ${root_tmp}/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
RUN
PATH="/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"
/usr/share/elasticsearch/bin/plugin -i elasticsearch/license/latest  
RUN
PATH="/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"
/usr/share/elasticsearch/bin/plugin -i elasticsearch/shield/latest  
RUN ln -s /usr/share/elasticsearch/config/shield /etc/elasticsearch/shield  
RUN curl -o /etc/elasticsearch/shield/users -SL
http://${fileshared}/elasticsearch/users  
RUN curl -o /etc/elasticsearch/shield/users_roles -SL
http://${fileshared}/elasticsearch/users_roles  
RUN curl -o /etc/elasticsearch/shield/license.json -SL
http://${fileshared}/elasticsearch/license.json  
RUN
PATH="/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"
/usr/share/elasticsearch/bin/plugin -i elasticsearch/marvel/latest  
#RUN /sbin/sysctl -w 'vm.swappiness=1'  
RUN echo "hello"  
EXPOSE 9200 9300  
ENTRYPOINT ["/bin/bash", "/root/tmp/run.sh"]  
  

