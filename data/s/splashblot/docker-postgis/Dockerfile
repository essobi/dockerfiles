FROM postgres:9.5  
MAINTAINER Juanjo Mata <juanjo.mata@gmail.com>  
  
ENV POSTGIS_MAJOR 2.3  
ENV POSTGIS_VERSION 2.3.3+dfsg-1.pgdg80+1  
RUN mkdir -p /data/backups  
VOLUME /data/backups  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts \  
postgis-2.3 \  
postgresql-server-dev-$PG_MAJOR \  
postgresql-plpython-$PG_MAJOR \  
postgresql-$PG_MAJOR-plproxy \  
ca-certificates \  
python-pip \  
python-dev \  
build-essential \  
automake \  
git-core \  
git \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip  
RUN pip install --upgrade virtualenv  
  
# Install rvm  
ENV PATH
$PATH:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
#RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 && \  
RUN gpg --keyserver hkp://http-keys.gnupg.net/ --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
curl -L
https://raw.githubusercontent.com/wayneeseguin/rvm/stable/binscripts/rvm-
installer | bash -s stable --ruby && \  
echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc && \  
/bin/bash -l -c rvm requirements && \  
echo rvm_max_time_flag=15 >> ~/.rvmrc && \  
/bin/bash -l -c 'rvm install 2.2.3' && \  
/bin/bash -l -c 'rvm use 2.2.3 --default' && \  
ln -s /usr/local/rvm/rubies/ruby-2.2.3/bin/ruby /usr/bin && \  
rm -rf /usr/local/rvm/src  
  
# Install stable CartoDB (#TODO: here best?) extension  
ENV CDB_STABLE_VERSION 0.20.0  
RUN git clone https://github.com/CartoDB/cartodb-postgresql && \  
cd cartodb-postgresql && \  
git checkout $CDB_STABLE_VERSION && \  
PGUSER=postgres make install  
  
# Install LATEST crankshaft (#TODO: here best?) extension  
ENV CRANKSHAFT_STABLE_VERSION 0.6.1  
RUN git clone https://github.com/CartoDB/crankshaft && \  
cd crankshaft && \  
git checkout $CRANKSHAFT_LATEST_VERSION && \  
PGUSER=postgres make install  
  
# Geocoder SQL client + server  
RUN git clone https://github.com/CartoDB/data-services.git && \  
cd /data-services/geocoder/extension && PGUSER=postgres make all install && cd
/ && \  
git clone https://github.com/CartoDB/dataservices-api.git && \  
cd /dataservices-api/server/extension && \  
PGUSER=postgres make install && cd ../lib/python/cartodb_services && \  
pip install -r requirements.txt && pip install . && \  
cd ../../../../client && PGUSER=postgres make install  
  
# Data observatory extension  
RUN git clone https://github.com/CartoDB/observatory-extension.git && \  
cd /observatory-extension && make install  
  
RUN mkdir -p /docker-entrypoint-init.d  
COPY ./01-init-crontab.sh /docker-entrypoint-init.d/01_crontab.sh  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./01-initdb-postgis.sh /docker-entrypoint-initdb.d/01_postgis.sh  
COPY ./02-initdb-cartodb_pgsql.sh /docker-entrypoint-
initdb.d/02_cartodb_pgsql.sh  
COPY ./03-initdb-cartodb_crankshaft.sh /docker-entrypoint-
initdb.d/03_cartodb_crankshaft.sh  
COPY ./04-initdb-metabase.sh /docker-entrypoint-initdb.d/04_metabase.sh  
COPY ./05-initdb-webodm.sh /docker-entrypoint-initdb.d/05_webodm.sh  
COPY ./06-initdb-carto_geocoder.sh /docker-entrypoint-
initdb.d/06_carto_geocoder.sh  
COPY ./07-initdb-cachet.sh /docker-entrypoint-initdb.d/07_cachet.sh  
COPY ./08-initdb-ag_tracker.sh /docker-entrypoint-initdb.d/08-ag_tracker.sh  
COPY ./09-initdb-openduty.sh /docker-entrypoint-initdb.d/09-openduty.sh  
  
COPY docker-entrypoint-cron.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint-cron.sh / # backwards compat  

