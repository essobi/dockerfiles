FROM tor2/centos-source-freezer-base:4.0.0  
MAINTAINER Kolla Project (https://launchpad.net/kolla)  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install mod_wsgi httpd && yum clean all  
  
RUN sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
#ADD freezer-api-archive /freezer-api-source  
RUN mkdir -p /freezer-api-source && git clone https://github.com/Inspur-
ocata/freezer-api.git -b stable/ocata /freezer-api-source/freezer-api  
RUN ln -s freezer-api-source/* freezer-api \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /freezer-api \  
&& cp -r /freezer-api/etc/freezer/* /etc/freezer/  
  
COPY extend_start.sh /usr/local/bin/kolla_freezer_extend_start  
RUN chmod 755 /usr/local/bin/kolla_freezer_extend_start  
  

