FROM centos:7  
MAINTAINER Bharat Akkinepalli <bharatak@thoughtworks.com>  
ENV REFRESHED_AT 2015-05-02T07:24  
RUN yum -y install python-psycopg2 python-lxml PyXML python-setuptools
libxslt-python pytz \  
python-matplotlib python-babel python-mako python-dateutil python-psycopg2 \  
pychart pydot python-reportlab python-devel python-imaging python-vobject \  
hippo-canvas-python mx python-gdata python-ldap python-openid \  
python-werkzeug python-vatnumber pygtk2 glade3 pydot python-dateutil \  
python-matplotlib pygtk2 glade3 pydot python-dateutil python-matplotlib \  
python python-devel python-psutil python-docutils make\  
automake gcc gcc-c++ kernel-devel byacc flashplugin-nonfree poppler-utils
pywebdav libyaml-devel tar wget unzip;yum clean all  
  
RUN curl -SL
https://www.dropbox.com/s/wjf7jlcm4c3txbc/openerp-7.0-20130301-002301.tar.gz |
tar xzf - -C /opt/  
  
WORKDIR /opt/openerp-7.0-20130301-002301  
  
RUN [ "python", "setup.py", "-q", "install" ]  
  
RUN adduser openerp  
  
ADD setup-artifacts.sh /tmp/setup-artifacts.sh  
  
RUN chmod +x /tmp/setup-artifacts.sh  
  
RUN /tmp/setup-artifacts.sh erp  
  
EXPOSE 8069  
VOLUME [ "/opt/openerp-7.0-20130301-002301" ]  
  
USER openerp  
  
CMD [ "sh", "-c" ,"openerp-server --without-demo all --db_user ${DB_USER}
\--db_host ${DB_HOST}" ]

