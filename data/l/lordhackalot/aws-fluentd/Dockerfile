FROM centos:6  
MAINTAINER nattapon <lordhackalot@gmail.com>  
  
#RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
#RUN rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
#RUN sed -i -e "s|^;date.timezone =.*$|date.timezone = Asia/Bangkok|"
/etc/php.ini  
ENV fileshared 52.74.40.153  
#RUN rpm -i http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-
release-1.0-11.ius.centos6.noarch.rpm  
RUN rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -i http://${fileshared}/python/ius-
release-1.0-11.ius.centos6.noarch.rpm  
RUN yum groupinstall -y "Development tools"  
RUN yum install -y sudo tar libcurl-devel GeoIP GeoIP-devel python-devel
postgresql-devel  
RUN sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
RUN ulimit -n 65536  
  
ENV root_tmp /root/tmp  
RUN mkdir -p $root_tmp && curl -o ${root_tmp}/td-agent.conf -SL
http://${fileshared}/fluentd/td-agent.conf  
RUN curl -o ${root_tmp}/Python-2.7.6.tar.xz -SL
http://${fileshared}/fluentd/Python-2.7.6.tar.xz  
RUN curl -o ${root_tmp}/run.sh -SL http://${fileshared}/fluentd/run.sh  
RUN curl -o ${root_tmp}/td-agent-2.1.5-1.x86_64.rpm -SL
http://${fileshared}/fluentd/td-agent-2.1.5-1.x86_64.rpm && \  
yum localinstall -y ${root_tmp}/td-agent-2.1.5-1.x86_64.rpm  
RUN ls -l ${root_tmp}/td-agent-2.1.5-1.x86_64.rpm  
RUN cp /etc/td-agent/td-agent.conf /etc/td-agent/td-agent.conf.orig && cp -f
${root_tmp}/td-agent.conf /etc/td-agent/  
RUN ln -s /usr/bin/gcc /usr/bin/gcc44  
  
RUN /usr/sbin/td-agent-gem install fluent-plugin-elasticsearch  
RUN /usr/sbin/td-agent-gem install fluent-plugin-format  
RUN /usr/sbin/td-agent-gem install fluent-plugin-woothee  
RUN /usr/sbin/td-agent-gem install fluent-plugin-forest  
RUN /usr/sbin/td-agent-gem install fluent-plugin-record-reformer  
RUN /usr/sbin/td-agent-gem install fluent-plugin-geoip -v 0.4.0  
  
RUN yum install -y python27 python27-devel python27-setuptools
python27-mod_wsgi  
RUN curl -o ${root_tmp}/get-pip.py -sSL http://${fileshared}/python/get-pip.py  
RUN cd ${root_tmp} && python get-pip.py  
RUN pip install virtualenv  
RUN curl -o ${root_tmp}/requirements.txt -sSL
http://${fileshared}/python/requirements.txt  
RUN curl -o ${root_tmp}/logger.tgz -sSL http://${fileshared}/python/logger.tgz  
RUN cd /opt && gzip -dc ${root_tmp}/logger.tgz | tar xvf -  
RUN virtualenv --python=/usr/bin/python2.7 /opt/venv  
RUN source /opt/venv/bin/activate  
RUN pip install -r /opt/logger/requirements.txt || echo "true"  
#RUN cd /opt && virtualenv --python=/usr/bin/python2.7 venv && source
/opt/venv/bin/activate && pip install -r /opt/logger/requirements.txt  
EXPOSE 8888 24224  
ENTRYPOINT ["/bin/bash", "/root/tmp/run.sh"]  
  

