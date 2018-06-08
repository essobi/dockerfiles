FROM centos/httpd-24-centos7  
  
ENV SUMMARY="BDR PostgreSQL Documentation" \  
DESCRIPTION="BDR PostgreSQL Documentation as it seen in http://bdr-
project.org/docs/stable/ \  
The image is based on centos/httpd-24-centos7 to run unprivileged httpd
container."  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="BDR PostgreSQL Documentation" \  
io.openshift.expose-services="8080:http,8443:https" \  
io.openshift.tags="documentation,docs,postgresql,bdr" \  
name="dockerized-docs/bdr-postgresql" \  
maintainer="Genadi Postrilko <genadipost@gmail.com>"  
  
ENV BDR_PG_VERSION=REL9_4_17-1  
ENV BDR_PLUGIN_VERSION=1.0.5  
ENV PG_CONFIG /usr/local/pgsql/bin/pg_config  
ENV PATH /usr/local/pgsql/bin/:"$PATH"  
user root  
  
WORKDIR /opt/app-root/src/  
  
RUN yum -y install git gcc gcc-c++ readline-devel zlib-devel bison flex flex-
devel \  
openjade texlive-jadetex docbook-dtds docbook-style-dsssl docbook-style-xsl  
  
RUN curl -L https://github.com/2ndQuadrant/bdr-postgres/archive/bdr-
pg/$BDR_PG_VERSION.tar.gz -o /opt/app-root/src/bdr-pg-$BDR_PG_VERSION.tar.gz
&& \  
curl -L https://github.com/2ndQuadrant/bdr/archive/bdr-
plugin/$BDR_PLUGIN_VERSION.tar.gz -o /opt/app-root/src/bdr-
plugin-$BDR_PLUGIN_VERSION.tar.gz && \  
tar -xvf bdr-pg-$BDR_PG_VERSION.tar.gz -C . && \  
tar -xvf bdr-plugin-$BDR_PLUGIN_VERSION.tar.gz -C .  
  
WORKDIR /opt/app-root/src/bdr-postgres-bdr-pg-$BDR_PG_VERSION  
  
RUN ./configure && \  
make && \  
make install  
  
USER default  
  
WORKDIR /opt/app-root/src/bdr-bdr-plugin-$BDR_PLUGIN_VERSION  
  
RUN ./configure && \  
make -j4 -s doc  
  
RUN mv doc/html/* /var/www/html/  
  
RUN rm -rf /opt/app-root/src/{bdr-pg-$BDR_PG_VERSION.tar.gz, bdr-
plugin-$BDR_PLUGIN_VERSION.tar.gz, bdr-postgres-bdr-pg-$BDR_PG_VERSION, bdr-
bdr-plugin-$BDR_PLUGIN_VERSION}  
  
CMD ["/usr/bin/run-httpd"]  

