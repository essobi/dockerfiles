FROM amazonlinux:1  
# Add mongo repo  
COPY mongodb-org-3.6.repo /etc/yum.repos.d/  
RUN yum install -y wget curl  
# Get Node and Yarn  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -  
RUN wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo  
RUN wget
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-6-x86_64/pgdg-
ami201503-96-9.6-2.noarch.rpm  
RUN rpm -i pgdg-ami201503-96-9.6-2.noarch.rpm  
RUN yum update -y  
RUN yum install -y mongodb-org gcc gcc-c++ make tcl git nodejs yarn jemalloc
vim postgresql96 postgresql96-server postgresql96-devel postgresql96-contrib
postgresql96-docs  
RUN mkdir -p /data/db  
RUN chown -R mongod:mongod /data  
RUN sleep 10  
# Not really necessary, but mimicking an auth configuration (more rights than
real curbmap test user has)  
COPY testuser.js /  
COPY testdb.js /  
COPY setup_mongo.sh /  
COPY mongod.conf /etc/  
RUN chmod u+x setup_mongo.sh  
RUN /setup_mongo.sh  
# Restart Mongo with auth  
RUN service mongod restart  
WORKDIR /  
COPY setup_network.sh /  
RUN chmod 755 /setup_network.sh  
RUN /setup_network.sh  
# Set up postgres  
COPY setup_postgres.sh /  
RUN chmod a+x /setup_postgres.sh  
# Make the services directory you will be loading your local files into  
RUN mkdir /services  
WORKDIR /  
RUN sed -i 's/5432/9020/g' /etc/init.d/postgresql96  
RUN service postgresql96 initdb  
# Just like it is on the actual server  
RUN sed -i 's/\\#port = 5432/port = 9020/g'
/var/lib/pgsql96/data/postgresql.conf  
COPY builddb.sql /  
RUN service postgresql96 stop  
RUN service postgresql96 start && su postgres -c /setup_postgres.sh  
RUN useradd -ms /bin/bash testing  
RUN sed -i '80s/peer/md5/g' /var/lib/pgsql96/data/pg_hba.conf  
RUN sed -i 's/ident/md5/g' /var/lib/pgsql96/data/pg_hba.conf  
RUN service postgresql96 start  
EXPOSE 8081  
EXPOSE 8080  
EXPOSE 9020  

