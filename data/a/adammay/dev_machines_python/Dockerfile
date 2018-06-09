FROM adammay/dev_machines_base:latest  
MAINTAINER Adam May <adammay@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
libmysqlclient-dev \  
libxml2-dev \  
libxslt1-dev \  
libzmq5 \  
libzmq3-dev \  
python3 \  
python3-dev \  
python3-pip \  
python3-zmq \  
sqlite \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
Run pip3 install ipython jupyter lxml sqlalchemy nose nose_parameterized ipdb
pandas numpy mysqlclient mycli  
  
# Default port for ipython notebook  
EXPOSE 8888  

