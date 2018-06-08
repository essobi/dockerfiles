FROM centos/httpd-24-centos7  
  
ENV SUMMARY="Repmgr Documentation" \  
DESCRIPTION="Repmgr Documentation as it seen in https://repmgr.org/docs/ \  
The image is based on centos/httpd-24-centos7 to run unprivileged httpd
container."  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="Repmgr Documentation" \  
io.openshift.expose-services="8080:http,8443:https" \  
io.openshift.tags="documentation,docs,postgresql,repmgr" \  
name="dockerized-docs/repmgr" \  
maintainer="Genadi Postrilko <genadipost@gmail.com>"  
  
ENV PG_VERSION 9.6.8  
ENV REPMGR_VERSION 4.0.4  
ENV PG_CONFIG /usr/local/pgsql/bin/pg_config  
ENV PATH /usr/local/pgsql/bin/:"$PATH"  
user root  
  
WORKDIR /opt/app-root/src/  
  
RUN yum -y groupinstall "Development Tools" && \  
yum -y install yum-utils openjade docbook-dtds docbook-style-dsssl docbook-
style-xsl \  
readline-devel zlib-devel texlive-jadetex texlive-jadetex-doc  
  
RUN curl -L
https://github.com/2ndQuadrant/repmgr/archive/v$REPMGR_VERSION.tar.gz -o
repmgr-v$REPMGR_VERSION.tar.gz && \  
curl -L
https://ftp.postgresql.org/pub/source/v$PG_VERSION/postgresql-$PG_VERSION.tar.gz
-o postgresql-$PG_VERSION.tar.gz && \  
tar -xvf repmgr-v$REPMGR_VERSION.tar.gz -C . && \  
tar -xvf postgresql-$PG_VERSION.tar.gz -C .  
  
WORKDIR /opt/app-root/src/postgresql-$PG_VERSION  
  
RUN ./configure && \  
make && \  
make install  
  
WORKDIR /opt/app-root/src/repmgr-$REPMGR_VERSION  
  
RUN ./configure && \  
make install-doc  
  
RUN cp -r /usr/local/pgsql/share/doc/contrib/repmgr/* /var/www/html/  
  
RUN rm -rf /opt/app-root/src/{repmgr-v$REPMGR_VERSION.tar.gz,
postgresql-$PG_VERSION.tar.gz, postgresql-$PG_VERSION, repmgr-$REPMGR_VERSION}  
  
USER default  
  
CMD ["/usr/bin/run-httpd"]  

