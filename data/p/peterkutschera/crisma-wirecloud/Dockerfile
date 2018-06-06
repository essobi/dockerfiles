# 2014-11-04  
# Peter.Kutschera@ait.ac.at  
# docker build -t peterkutschera/crisma-wirecloud .  
#  
# There are 2 ways to use the wirecloud container:  
#  
# 1. Keep wirecloud data inside of the container - they will be lost when the
cointainer is replaced  
# docker run -P -d --name c_wirecloud --env WIRECLOUD_ADMIN_PASSWD=unknown
--link c_orion:orion peterkutschera/crisma-wirecloud  
#  
# 2. Keep wirecloud data in an extrea data store, e.g. under data/wirecloud  
# docker run -P -d --name c_wirecloud --env WIRECLOUD_ADMIN_PASSWD=unknown -v
$(pwd)/data/wirecloud:/wirecloud --link c_orion:orion peterkutschera/crisma-
wirecloud  
# Available ports:  
# 80: wireclound - login with user = admin, password = WIRECLOUD_ADMIN_PASSWD  
# 3000: NGSI proxy  
# see http://conwet.fi.upm.es/wirecloud/  
FROM centos:centos6  
MAINTAINER Peter.Kutschera@ait.ac.at  
  
ENV WIRECLOUD_ADMIN_PASSWD admin  
ENV DEFAULT_SILBOPS_BROKER 'http://pubsub.server.com:8080/silbops/CometAPI'  
RUN yum install -y epel-release && \  
yum install -y python-devel python-pip libxml2-devel libxslt-devel user-agents
django-relatives pytz && \  
yum install -y postgresql-server postgresql-devel python-psycopg2 && \  
yum install -y wget gcc git tar && \  
yum install -y httpd mod_wsgi  
  
RUN pip install "Django>=1.4,<1.6" "south<2.0" BeautifulSoup lxml
"django_compressor>=1.2" "rdflib>=3.2.0" requests>=2.0.0 pytz importlib  
  
# fix problem cron not able to run root cronjobsd  
#RUN perl -i.bak -p -e 's/^(session\s+required\s+pam_loginuid.so)\s*$/#\1\n/'
/etc/pam.d/crond  
# this version does not work!  
#RUN mkdir /home/src && \  
# cd /home/src && \  
# wget -q --no-check-certificate https://forge.fi-
ware.org/frs/download.php/849/APPS-Application-Mashup-Wirecloud-3.2.1.tar.gz
&& \  
# pip install APPS-Application-Mashup-Wirecloud-3.2.1.tar.gz && \  
# cd / && \  
# rm -rf /home/src  
#RUN mkdir /home/src && \  
# cd /home/src && \  
# pip install Pygments pyScss==1.2.0.post3 pycrypto whoosh>=2.5.6 markdown
regex user-agents django-relatives selenium>=2.41 importlib && \  
# git clone https://github.com/Wirecloud/wirecloud.git && \  
# cd wirecloud/src && \  
# python setup.py install  
# This is missing /opt/wirecloud_instance/static  
#RUN pip install wirecloud  
#RUN mkdir /home/src && \  
# cd /home/src && \  
# wget -q --no-check-certificate
https://pypi.python.org/packages/source/w/wirecloud/wirecloud-0.6.5.tar.gz &&
\  
# pip install wirecloud-0.6.5.tar.gz && \  
# pip install wirecloud-pubsub && \  
# cd && \  
# rm -rf /home/src  
RUN pip install wirecloud==0.7.2 wirecloud-pubsub  
  
# NGSI proxy:  
EXPOSE 3000  
RUN yum install -y nodejs npm && \  
mkdir /home/ngsi && \  
cd /home/ngsi && \  
git clone git://github.com/conwetlab/ngsijs.git && \  
cd ngsijs/ngsi-proxy && \  
npm install  
  
# See runAll.sh how to run the proxy  
# Correct settings using NGSI from within WireCloud:  
# orion: http://orion:1026/  
# NGSI proxy: http://localhost:3000/  
WORKDIR /opt  
RUN wirecloud-admin startproject wirecloud_instance  
  
# Edit /opt/wirecloud_instance/wirecloud_instance/settings.py  
RUN perl -i.bak -p -e "s/'ENGINE': 'django.db.backends.'/'ENGINE':
'django.db.backends.postgresql_psycopg2'/; \  
s/'NAME': ''/'NAME': 'wirecloud'/; \  
s/'USER': ''/'USER': 'wc_user'/; \  
s/'PASSWORD': ''/'PASSWORD': 'wc_passwd'/; \  
s{(STATIC_URL\s*=\s*)'/static/'}{\1'/wirecloud/static/'}; \  
s/'wirecloud.oauth2provider'/#'wirecloud.oauth2provider'/; \  
s/^(INSTALLED_APPS.*)$/\1\n 'wirecloud_pubsub',/"
/opt/wirecloud_instance/wirecloud_instance/settings.py  
  
# Needed for NGSI, so no longer remove them  
# s/'wirecloud.fiware'/#'wirecloud.fiware'/; \  
# correct problem ?  
RUN perl -i.bak -p -e 's/"FIWARE_IDM_SERVER":/#"FIWARE_IDM_SERVER":/'
/usr/lib/python2.6/site-packages/wirecloud/fiware/plugins.py  
  
RUN echo -e "\n# requestBroker\nDEFAULT_SILBOPS_BROKER =
'${DEFAULT_SILBOPS_BROKER}'\n\n" >>
/opt/wirecloud_instance/wirecloud_instance/settings.py  
RUN echo -e "\n# Create fully qualified URLs for the front-end client when
running behind a reverse proxy:\nUSE_X_FORWARDED_HOST = True\n\n" >>
/opt/wirecloud_instance/wirecloud_instance/settings.py  
  
# needed if there is this service is running behind a https -> http provy  
RUN echo -e "\n# see
https://docs.djangoproject.com/en/1.4/ref/settings/\nSECURE_PROXY_SSL_HEADER =
('HTTP_X_FORWARDED_PROTOCOL', 'https')\nFORCE_PROTO = 'https'\n\n" >>
/opt/wirecloud_instance/wirecloud_instance/settings.py  
  
RUN cat /opt/wirecloud_instance/wirecloud_instance/settings.py  
  
RUN chmod +x /opt/wirecloud_instance/manage.py  
  
# fill wirecloud database, create user,...  
# To enable login run: /opt/wirecloud_instance/manage.py changepassword --help  
# this is needed to insert the password from the command line into the
database  
COPY usr/lib/python2.6/site-
packages/django/contrib/auth/management/commands/changepassword2secret.py
/usr/lib/python2.6/site-
packages/django/contrib/auth/management/commands/changepassword2secret.py  
  
# initialize postgresql and fill wirecloud database  
RUN service postgresql initdb  
  
# Edit /var/lib/pgsql/data/pg_hba.conf (At the beginning of the rules!)  
RUN perl -i.bak -p -e 's/(#\s*TYPE\s+DATABASE\s+USER\s+CIDR-
ADDRESS\s+METHOD)/\1\nlocal\twirecloud\twc_user\t\ttrust\nlocal\ttest_wirecloud\twc_user\t\ttrust
# only necessary for testing Wirecloud/' /var/lib/pgsql/data/pg_hba.conf  
  
# Test: Does this work?  
# service postgresql reload  
# psql wirecloud -U wc_user  
RUN /etc/init.d/postgresql restart; \  
su postgres -c "psql --command=\"create user wc_user with login password
'wc_passwd' superuser;\"" && \  
su postgres -c "createdb --owner=wc_user wirecloud" && \  
/opt/wirecloud_instance/manage.py syncdb --noinput && \  
/opt/wirecloud_instance/manage.py createsuperuser --username=admin
--email='need2@change.me' \--noinput && \  
/opt/wirecloud_instance/manage.py changepassword2secret admin
${WIRECLOUD_ADMIN_PASSWD} && \  
/opt/wirecloud_instance/manage.py migrate && \  
/opt/wirecloud_instance/manage.py collectstatic --noinput  
  
# This image offers wirecloud not under / but under /wirecloud.  
# while this is no problem for the server part the javascript running in the
browser dont know about.  
# So let's patch the javascript - at least where I idenified the problem
already  
# HistoryManager: this is the only one / within double quotes :-)  
RUN perl -i.bak -p -e 's{"/"}{"/wirecloud/"}'
/opt/wirecloud_instance/static/js/wirecloud/HistoryManager.js  
  
# There is also an problem with WirecloudWidgetAPI.js  
RUN perl -i.bak -p -e 's{\\(current\\[0\\] === "id"\\)}{((current[0] === "id")
|| (current[0] === "/id"))}'
/opt/wirecloud_instance/static/js/WirecloudAPI/WirecloudAPI.js  
# Check: grep 'current\\[0\\] === "id"'
/opt/wirecloud_instance/static/js/WirecloudAPI/WirecloudAPI.js  
# create cache  
RUN /opt/wirecloud_instance/manage.py compress --force || true  
  
# prepare usage of external volume  
RUN mkdir /opt/wirecloud_instance/wirecloud_instance/catalogue_resources.real
/opt/wirecloud_instance/wirecloud_instance/widget_files.real && \  
ln -sf /opt/wirecloud_instance/wirecloud_instance/catalogue_resources.real
/opt/wirecloud_instance/wirecloud_instance/catalogue_resources && \  
ln -sf /opt/wirecloud_instance/wirecloud_instance/widget_files.real
/opt/wirecloud_instance/wirecloud_instance/widget_files  
  
RUN chown -R apache:apache /opt/wirecloud_instance/  
  
# TEST: access DB using: psql -U wc_user wirecloud  
# TEST:  
#EXPOSE 8080  
#CMD /etc/init.d/postgresql start; \  
# /opt/wirecloud_instance/manage.py runserver 0.0.0.0:8080 --insecure  
COPY etc/httpd/conf.d/wirecloud.conf /etc/httpd/conf.d/wireclound.conf  
COPY var/www/html/index.html /var/www/html/index.html  
  
COPY root/bin/runAll.sh /root/bin/runAll.sh  
RUN chmod +x /root/bin/runAll.sh  
  
# Used for backup  
RUN mkdir -p /root/backup/data  
COPY root/backup/Makefile /root/backup/Makefile  
  
EXPOSE 80  
CMD ["/root/bin/runAll.sh"]  
  

