FROM mysql:latest  
  
  
RUN apt-get update && apt-get install -y git ca-certificates build-essential
libmysqlclient-dev libpcre3-dev && \  
  
git clone https://github.com/infusion/udf_infusion.git && \  
cd udf_infusion && \  
./configure && \  
make && \  
make install && \  
apt-get remove -y git ca-certificates build-essential libmysqlclient-dev
libpcre3-dev && \  
cat load.sql > /docker-entrypoint-initdb.d/load.sql && \  
cd .. && rm -rf udf_infusion && \  
apt-get clean && apt-get purge  

