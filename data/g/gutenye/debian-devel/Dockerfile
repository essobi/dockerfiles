FROM tianon/debian-devel  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 80572343 && \  
echo 'deb http://guten.me/debs debian main' | tee
/etc/apt/sources.list.d/guten.list && \  
apt-get update && \  
apt-get install -y aptly gutdeb && \  
rm -rf /var/lib/apt/lists/*  

