# Transmart 1.2 using hyve installation  
# cf https://wiki.transmartfoundation.org/pages/viewpage.action?pageId=6619205  
# last modified by Terry Weymouth on Dec 10, 2014  
FROM ubuntu:14.04  
MAINTAINER Karl Forner <karl.forner@quartzbio.com>  
  
  
### STEP 1  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 3375DA21 && \  
echo deb http://apt.thehyve.net/internal/ trusty main | \  
tee /etc/apt/sources.list.d/hyve_internal.list && apt-get update  
  
### STEP 2  
RUN apt-get install -y \  
make \  
curl \  
git \  
openjdk-7-jdk \  
groovy \  
php5-cli \  
php5-json \  
postgresql-9.3 \  
apache2 \  
tomcat7 \  
libtcnative-1 \  
transmart-r  
  
# ============== transmart WAR (web app archive) =================  
# N.B: put this as early as possible to make sure it is cached, and will not
be downloaded on any change  
# should be transmart.war.1.2.2.e.fg-fix  
ENV TRANSMART_URL
http://owncloud.etriks.org/public.php?service=files&t=fa3130b3ab0e2649489b641e8293e9c9&download  
RUN curl -# $TRANSMART_URL > /var/lib/tomcat7/webapps/transmart.war  
  
# ==================== setup USER transmart ====================  
# create home too  
RUN useradd -m transmart  
# sudo with no password  
RUN echo "transmart ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
ENV HOME /home/transmart  
  
USER transmart  
WORKDIR /home/transmart  
  
### STEP 3: transmart-data  
#RUN git clone --progress https://github.com/transmart/transmart-data.git && \  
# cd transmart-data && git checkout tags/v1.2.0  
RUN git clone \--progress https://github.com/transmart/transmart-data.git  
WORKDIR /home/transmart/transmart-data  
  
### STEP 4 and 5: configure transmart-data  
## Configure default locale: TODO, put it below, before transmart  
RUN sudo bash -c 'echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8'  
ENV LC_ALL en_US.UTF-8  
RUN php env/vars-ubuntu.php > vars  
  
### STEP 5: Create transmart database table-spaces and schema  
RUN sudo service postgresql start && \  
sudo -u postgres bash -c \  
"source vars; PGSQL_BIN=/usr/bin/ PGDATABASE=template1 make -C
ddl/postgres/GLOBAL tablespaces" && \  
bash -c "source vars && make -j6 postgres && \  
make -C ddl/postgres/META fix_permissions fix_owners fix_tablespaces"  
  
### STEP 6: Copy tranSMART configuration files  
RUN sudo bash -c "source vars; TSUSER_HOME=/usr/share/tomcat7/ make -C config/
install"  
  
# create the tomcat tmp dir  
RUN sudo mkdir /var/lib/tomcat7/tmp && sudo chown tomcat7:tomcat7
/var/lib/tomcat7/tmp  
  
# ### STEP 7: Install and run solr  
# karl: N.B, modified to only install  
RUN bash -c "source vars; make -C solr/ solr_home"  
# karl (from Florian): fix the solr port in groovy config  
RUN sudo perl -pi'.bak' -e 's/(def solrPort\s+=\s+)\d+/$1 8983/ '
/usr/share/tomcat7/.grails/transmartConfig/Config.groovy  
  
### STEP 8: Configure and start Rserve  
# karl: N.B, will just configure it for now  
RUN echo 'USER=tomcat7' | sudo tee /etc/default/rserve  
  
### STEP 9: Deploy tranSMART web application on tomcat.  
RUN echo 'JAVA_OPTS="-Xmx4096M -XX:MaxPermSize=1024M"' | sudo tee
/usr/share/tomcat7/bin/setenv.sh  
  
### STEP 10: Prepare ETL environment  
# # karl: need xz-utils to uncompress data  
RUN sudo apt-get install xz-utils  
  
#### apparently not needed, dixit Florian, but not sure...  
RUN bash -c 'source vars && \  
make -C env/ data-integration && \  
make -C env/ update_etl'  
  
# ### STEP 11: example studies  
# karl: fix, must update the git repo first and re-run data-integration  
#RUN git pull origin master && \  
#RUN bash -c 'source vars && make -C env/ data-integration'  
#COPY GSE19976.zip /home/transmart/transmart-data/  
#COPY v12_GSE19976_clin.sh /home/transmart/transmart-data/  
RUN sudo rm -f /var/run/postgresql/.s* /var/run/postgresql/*
/var/lib/postgresql/9.3/main/postmaster.pid && \  
sudo service postgresql start && bash -c 'source vars && \  
make -C samples/postgres load_clinical_GSE8581 load_ref_annotation_GSE8581 \  
load_expression_GSE8581'&& \  
sudo service postgresql stop  
  
# postgres cleanup: -> non clean shutdown  
RUN sudo rm -f /var/run/postgresql/.s* /var/run/postgresql/*
/var/lib/postgresql/9.3/main/postmaster.pid  
  
########################### SUPERVISOR ######################################  
RUN sudo apt-get install -y --no-install-recommends supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
USER root  
  
# ==================== karl: configure postgres for external connections
========  
# replace existing listen_addresses entry by our own  
RUN perl -i -pe "s/.*listen_addresses.+/listen_addresses = '*'/"
/etc/postgresql/9.3/main/postgresql.conf  
# allow any connection to postgres  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
ENV TERM xterm  
  
# for tomcat  
EXPOSE 8080  
# for solr  
EXPOSE 8983  
# for postgres  
EXPOSE 5432  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  
  

