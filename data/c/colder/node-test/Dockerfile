FROM node  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
1614552E5765227AEC39EFCFA7E00EF33A8F2399 && \  
echo "deb http://download.rethinkdb.com/apt jessie main" >
/etc/apt/sources.list.d/rethinkdb.list && \  
apt-get update && \  
apt-get install -y rethinkdb && \  
rm -rf /var/lib/apt/lists/*  

