FROM tomcat:7-jre8  
MAINTAINER Alexander De Leon <me@alexdeleon.name>  
  
# Install dependencies  
RUN apt-get update && apt-get -y install build-essential postgresql php5 sudo
rsync supervisor  
  
RUN apt-get update && apt-get -y install r-base libcairo2-dev  
  
#Install R dependencies  
ADD biocLite.R /tmp/biocLite.R  
ADD install-packages.R /tmp/install-packages.R  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript /tmp/install-packages.R  
  
# Set up locale  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
# Install transmartApp WAR  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
ADD https://ci.transmartfoundation.org/browse/DEPLOY-
TRAPP-14/artifact/shared/transmart.war/transmart.war
/usr/local/tomcat/webapps/ROOT.war  
  
# Install transmart-data  
ADD https://github.com/transmart/transmart-data/archive/v1.2.4.tar.gz
/opt/transmart-data.tar.gz  
RUN cd /opt; tar xzf transmart-data.tar.gz  
ADD vars /opt/transmart-data-1.2.4/vars  
RUN chown -R postgres:postgres /opt/transmart-data-1.2.4  
  
# Init DB  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private &&
/etc/init.d/postgresql start && su postgres -c "cd /opt/transmart-data-1.2.4
&& . ./vars && skip_fix_tablespaces=1 make -j4"  
# Create config files for transmartApp  
RUN cd /opt/transmart-data-1.2.4 && . ./vars && make -C config install && make
-C solr/ solr_home  
  
# Install groovy  
ADD http://dl.bintray.com/groovy/maven/groovy-binary-2.4.3.zip /opt/transmart-
data-1.2.4/env/groovy-binary-2.4.3.zip  
RUN cd /opt/transmart-data-1.2.4/env/; unzip groovy-binary-2.4.3.zip  
ENV PATH /opt/transmart-data-1.2.4/env/groovy-2.4.3/bin:$PATH  
  
# Install Kettle  
ADD
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/5.3/pdi-
ce-5.3.0.0-213.zip?r=http%3A%2F%2Fcommunity.pentaho.com%2Fprojects%2Fdata-
integration%2F&ts=1432137602&use_mirror=softlayer-ams /opt/transmart-
data-1.2.4/env/kettle.zip  
RUN cd /opt/transmart-data-1.2.4/env/; unzip kettle.zip  
  
# Dowload tranSMART-ETL  
ADD https://github.com/thehyve/tranSMART-ETL/archive/v1.2.1.zip
/opt/transmart-etl.zip  
RUN cd /opt; unzip transmart-etl.zip  
  
# Download sample data  
RUN cd /opt/transmart-data-1.2.4; . ./vars && make update_datasets  
  
# Create supervisor config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD load.sh /usr/local/bin/load  
RUN chmod +x /usr/local/bin/load  
  
ADD start-postgres.sh /start-postgres.sh  
RUN chmod +x /start-postgres.sh  
  
# work around for AUFS bug  
# as per https://github.com/docker/docker/issues/783#issuecomment-56013588  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private  
  
# Ports for postgresql and tomcat are exposed  
#postgresql  
EXPOSE 5432  
#transmart  
EXPOSE 8080  
#solr  
EXPOSE 8983  
#rserver  
EXPOSE 6311  
CMD ["/usr/bin/supervisord"]

