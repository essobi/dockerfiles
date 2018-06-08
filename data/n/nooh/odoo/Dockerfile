FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y -q postgresql  
RUN apt-get install -y -q python-cups python-dateutil python-decorator python-
docutils python-feedparser \  
python-gdata python-geoip python-gevent python-imaging python-jinja2 python-
ldap python-libxslt1 \  
python-lxml python-mako python-mock python-openid python-passlib python-psutil
python-psycopg2 \  
python-pybabel python-pychart python-pydot python-pyparsing python-pypdf
python-reportlab python-requests \  
python-simplejson python-tz python-unicodecsv python-unittest2 python-
vatnumber python-vobject \  
python-werkzeug python-xlwt python-yaml wkhtmltopdf  
  
RUN apt-get install -y -q git  
  
RUN git clone https://www.github.com/odoo/odoo --depth 1 \--branch 8.0
\--single-branch  
  
RUN useradd -ms /bin/bash odoo  
  
ADD odoo-server /etc/init.d/  
RUN sudo chmod 755 /etc/init.d/odoo-server  
ADD openerp-server.conf /etc/  
ADD odoo-start.sh .  
RUN sudo chmod 755 odoo-start.sh  
ADD odoo-user.sh .  
RUN sudo chmod 755 odoo-user.sh  

