# This Source Code Form is subject to the terms of the Mozilla Public  
# License, v. 2.0. If a copy of the MPL was not distributed with this  
# file, You can obtain one at http://mozilla.org/MPL/2.0/.  
#  
# This Source Code Form is "Incompatible With Secondary Licenses", as  
# defined by the Mozilla Public License, v. 2.0.  
FROM bugzilla/bugzilla-base  
MAINTAINER David Lawrence <dkl@mozilla.com>  
  
# Environment configuration  
ENV BUGZILLA_USER bugzilla  
ENV BUGS_DB_DRIVER mysql  
ENV GITHUB_BASE_GIT https://github.com/bugzilla/bugzilla  
ENV GITHUB_BASE_BRANCH master  
ENV PATCH_DIR /patch_dir  
  
# Distribution package installation  
COPY conf/rpm_list /  
RUN yum -y -q install `cat /rpm_list` && \  
yum clean all  
  
# User configuration  
RUN useradd -m -G wheel -u 1000 -s /bin/bash $BUGZILLA_USER \  
&& passwd -u -f $BUGZILLA_USER \  
&& echo "bugzilla:bugzilla" | chpasswd  
  
# Apache configuration  
COPY conf/bugzilla.conf /etc/httpd/conf.d/bugzilla.conf  
RUN chown root.root /etc/httpd/conf.d/bugzilla.conf && \  
chmod 440 /etc/httpd/conf.d/bugzilla.conf  
  
# MySQL pre-configuration  
COPY conf/my.cnf /etc/my.cnf  
RUN chmod 644 /etc/my.cnf && \  
chown root.root /etc/my.cnf && \  
rm -rf /etc/mysql && \  
rm -rf /var/lib/mysql/*  
RUN /usr/bin/mysql_install_db --user=$BUGZILLA_USER \--basedir=/usr
--datadir=/var/lib/mysql  
  
# PostgreSQL pre-configuration  
ENV PGDATA /var/lib/pgsql/data  
ENV PGPORT 5432  
RUN su postgres -c "initdb"  
RUN echo "host all all 0.0.0.0/0 trust" >> $PGDATA/pg_hba.conf  
COPY conf/postgresql.conf $PGDATA  
  
# Copy setup and test scripts  
RUN cpanm -l $BUGZILLA_LIB \--quiet --notest Test::WWW::Selenium && rm -rf
~/.cpanm  
COPY scripts/* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
  
# Testing scripts for CI  
ADD https://selenium-release.storage.googleapis.com/2.53/selenium-server-
standalone-2.53.1.jar /selenium-server.jar  
  
# Networking  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
EXPOSE 80  
EXPOSE 5900  
CMD ["runtests.sh"]  

