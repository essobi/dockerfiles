FROM ubuntu:12.04  
MAINTAINER Leon Ho  
  
# Install dependencies for ACS installation  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y python-software-properties wget  
  
RUN apt-get install -y apache2  
# In /etc/apache2/apache2.conf add ServerName altubutu01  
RUN /etc/init.d/apache2 restart  
# Fix certificates  
RUN apt-get install -y ssl-cert  
# RUN make-ssl-cert generate-default-snakeoil --force-overwrite  
# install mod_wsgi  
RUN apt-get install -y libapache2-mod-wsgi  
RUN ln -s /etc/apache2/mods-available/proxy.conf /etc/apache2/mods-
enabled/proxy.conf  
RUN ln -s /etc/apache2/mods-available/proxy.load /etc/apache2/mods-
enabled/proxy.load  
RUN /etc/init.d/apache2 restart  
  
RUN apt-get install -y sqlite3  
RUN apt-get install -y git  
RUN apt-get install -y postfix  
ENV DEBIAN_FRONTEND noninteractive  
  
# POSTGRES  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# Add PostgreSQL's repository. It contains the most recent stable release  
# of PostgreSQL, ``9.3``.  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# Install ``python-software-properties``, ``software-properties-common`` and
PostgreSQL 9.3  
# There are some warnings (in red) that show up during the build. You can hide  
# them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3  
  
# Note: The official Debian and Ubuntu images automatically ``apt-get clean``  
# after each ``apt-get``  
# Create a PostgreSQL role named ``docker`` with ``docker`` as the password
and  
# then create a database `docker` owned by the ``docker`` role.  
# Note: here we use ``&&\\`` to run commands one after the other - the ``\\``  
# allows the RUN command to span multiple lines.  
RUN su - postgres -c "/etc/init.d/postgresql start && psql --command \"CREATE
USER acsuser WITH SUPERUSER PASSWORD 'acspw';\" && createdb -O acsuser acs"  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Apache OpenOffice  
# RUN add-apt-repository ppa:upubuntu-com/office  
# RUN apt-get update  
# RUN apt-get install -y unzip bzip2  
# RUN apt-get install -y openoffice  
# Install OpenOffice - headless/server-mode  
RUN apt-get install -y libxt6  
RUN apt-get install -y libxrender1  
RUN wget
http://sourceforge.net/projects/openofficeorg.mirror/files/4.1.1/binaries/en-
US/Apache_OpenOffice_4.1.1_Linux_x86-64_install-deb_en-US.tar.gz  
RUN tar -xvf Apache_OpenOffice*.tar.gz  
RUN dpkg -i en-US/DEBS/*.deb  
RUN dpkg -i en-US/DEBS/desktop-integration/*.deb  
  
# Azul Zulu OpenJDK 8  
# RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
0x219BD9C9  
# RUN apt-add-repository "deb http://repos.azulsystems.com/ubuntu stable main"  
# RUN apt-get update  
# RUN apt-get install -y zulu-8  
# Install Oracle Java 8  
RUN apt-add-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu
precise main"  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
# Accept Oracle lisence automatically  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
# ACS stuff  
RUN adduser acs-user  
RUN su - acs-user -c "git clone https://github.com/altran/Awesome-Competence-
System.git "  
RUN su - acs-user -c "ln -s Awesome-Competence-System acs"  
  
# ACS - SOLR index  
RUN adduser solr  
RUN su - solr -c "/usr/bin/wget -O /home/solr/solr-4.4.0.tgz -q -N
https://archive.apache.org/dist/lucene/solr/4.4.0/solr-4.4.0.tgz"  
RUN su - solr -c "tar -zxvf solr-4.4.0.tgz"  
  
# And the django stack for ACS  
RUN apt-get install -y python-django  
ADD acs.conf /etc/apache2/sites-available/acs.conf  
RUN ln -s /etc/apache2/sites-available/acs.conf /etc/apache2/sites-
enabled/acs.conf  
ADD .htaccess /home/acs-user/acs/cvbase/.htaccess  
ADD .htaccess /home/acs-user/acs/password  
  
# Django modules  
RUN apt-get install -y python-pip python-lxml libxml2-dev libxslt-dev python-
imaging libpq-dev python-dev  
  
# pip modules  
RUN pip install Django==1.6.2  
RUN pip install django-haystack  
RUN pip install django-admin-bootstrapped==1.6.4  
RUN pip install pysolr==3.2.0  
RUN pip install appy==0.8.4  
RUN pip install django-webodt psycopg2  
RUN pip install lxml --upgrade  
  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# Whatever this is.. :)  
RUN apt-get install -y libgtk2.0-0:i386 libidn11:i386 libglu1-mesa:i386  
  
# Django directories  
RUN mkdir /var/log/django  
RUN chgrp www-data /var/log/django  
RUN chown www-data /var/log/django  
RUN mkdir /var/www/static  
RUN chgrp www-data /var/www/static  
RUN chown www-data /var/www/static  
RUN mkdir /var/www/media  
RUN chgrp www-data /var/www/media  
RUN chown www-data /var/www/media  
RUN mkdir /var/www/media/photos  
RUN chgrp www-data /var/www/media/photos  
RUN chown www-data /var/www/media/photos  
RUN mkdir /var/www/media/templates  
RUN chgrp www-data /var/www/media/templates  
RUN chown www-data /var/www/media/templates  
  
RUN touch /var/log/django/logfile  
RUN chgrp www-data /var/log/django/logfile  
RUN chown www-data /var/log/django/logfile  
  
RUN /etc/init.d/apache2 restart  
  
# Not ported from ansible yet..  
# https://github.com/Cantara/Awesome-Competence-System-
Provisioning/blob/master/roles/django/tasks/main.yml  
ADD localsettings.py /home/acs-user/acs/cvapp/localsettings.py  
RUN service postgresql start && sleep 5 && python /home/acs-
user/acs/cvapp/manage.py syncdb --noinput  
  
# name: Python Collect static files into /var/www/static  
# shell: echo "yes" | python /home/acs-user/acs/cvapp/manage.py collectstatic  
RUN echo "yes" | python /home/acs-user/acs/cvapp/manage.py collectstatic  
#  
# name: Copy Solr password file  
# template: src=solr-password.jinja dest=/home/acs-user/password backup=yes
owner=acs-user group=www-data mode=644  
# name: Index ACS site in Solr  
# shell: echo "y" | python /home/acs-user/acs/cvapp/manage.py rebuild_index  
ADD run_solr.sh /home/solr/run_solr.sh  
RUN chmod 755 /home/solr/run_solr.sh  
# RUN service postgresql start && /home/solr/run_solr.sh && sleep 5 && python
/home/acs-user/acs/cvapp/manage.py rebuild_index --noinput  
# name: Set file ownership of all acs correctly  
# file: state=file path={{item}} owner=acs-user group=www-data mode=644  
# with_items:  
# - /home/acs-user/acs/cvapp/localsettings.pyc  
# - /home/acs-user/acs/cvapp/settings.pyc  
RUN chgrp www-data /home/acs-user/acs/cvapp/localsettings.pyc  
RUN chown acs-user /home/acs-user/acs/cvapp/localsettings.pyc  
RUN chgrp www-data /home/acs-user/acs/cvapp/settings.pyc  
RUN chown acs-user /home/acs-user/acs/cvapp/settings.pyc  
RUN chmod 644 /home/acs-user/acs/cvapp/settings.pyc  
RUN chmod 644 /home/acs-user/acs/cvapp/localsettings.pyc  
RUN chown -R solr /home/solr  
  
# Sending mail  
RUN apt-get install -y -q --force-yes postfix  
  
# Expose port 80 and 443  
EXPOSE 80 443  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN ln -s /etc/supervisor/conf.d/supervisord.conf /etc/supervisord.conf  
CMD ["/usr/bin/supervisord"]  
  

