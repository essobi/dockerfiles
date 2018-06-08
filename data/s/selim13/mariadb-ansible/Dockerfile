FROM mariadb:10.1  
  
RUN apt-get update && apt-get install -y python2.7 python-mysqldb --no-
install-recommends && rm -rf /var/lib/apt/lists/*  
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 10  

