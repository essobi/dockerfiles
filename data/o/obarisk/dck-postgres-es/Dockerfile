FROM postgres:latest  
  
ENV PG_VER 10  
  
RUN apt-get update && \  
apt-get install -y postgresql-plpython-${PG_VER} postgresql-${PG_VER}-plr && \  
apt-get install -y postgresql-${PG_VER}-python3-multicorn && \  
apt-get install -y postgresql-${PG_VER}-plsh && \  
apt-get install -y postgresql-${PG_VER}-pldebugger && \  
apt-get install -y postgresql-${PG_VER}-jsquery && \  
apt-get install -y python3-setuptools && \  
apt-get install -y git curl ssl-cert && \  
git clone https://github.com/Mikulas/pg-es-fdw /tmp/pg-es-fdw && \  
cd /tmp/pg-es-fdw && \  
python3 setup.py install && \  
cd - && \  
rm -rf /tmp/pg-es-fdw && \  
rm -rf /var/lib/apt/lists/*  
  
ADD docker-entrypoint-initdb.d /docker-entrypoint-initdb.d  

