FROM postgres:9.5  
  
MAINTAINER Yuri Zhylyuk <yuri@zhylyuk.com>  
  
RUN \  
# add columnar store extension cstore_fdw  
apt-get update && \  
apt-get -y install protobuf-c-compiler make git libprotobuf-c0-dev postgresql-
server-dev-9.5 libpq-dev gcc apt-utils && \  
git clone https://github.com/citusdata/cstore_fdw.git && \  
cd cstore_fdw && \  
PATH=/usr/lib/postgresql/9.5/bin/:$PATH make && \  
PATH=/usr/lib/postgresql/9.5/bin/:$PATH make install && \  
echo "shared_preload_libraries = 'cstore_fdw'" >>
/var/lib/postgresql/data/postgresql.conf && \  
cd .. && \  
rm -rf cstore_fdw  
RUN \  
# add multicorn/SqlAlchemyFdw foreign table extension and plpython3 with some
libraries:  
apt-get -y install python3 && \  
PYTHON=/usr/bin/python3 && \  
apt-get -y install python3-dev python3-pip postgresql-plpython3-9.5
postgresql-9.5-python3-multicorn && \  
pip3 install numpy pandas SQLAlchemy && \  
pip3 install pymysql requests boto rethinkdb lxml  
RUN \  
# add foreign table extension mysql_fdw:  
git clone https://github.com/EnterpriseDB/mysql_fdw.git && \  
cd mysql_fdw && \  
apt-get -y install mysql-client libmysqlclient-dev && \  
PATH=/usr/lib/postgresql/9.5/bin/:$PATH make USE_PGXS=1 && \  
PATH=/usr/lib/postgresql/9.5/bin/:$PATH make USE_PGXS=1 install && \  
cd .. && \  
rm -rf mysql_fdw && \  
apt-get -y clean autoclean && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  

