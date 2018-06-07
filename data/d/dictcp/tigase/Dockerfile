# Ubuntu/precise is the main distribution  
FROM ubuntu:trusty  
  
# setup java ppa  
RUN rm -rvf /var/lib/apt/lists/*  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y libssl1.0.0 openssl postgresql-
client  
RUN apt-get install --no-install-recommends -y software-properties-common
python-software-properties  
RUN add-apt-repository ppa:webupd8team/java  
  
# add wget  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install --no-install-recommends -y wget oracle-java7-installer  
  
# download and install tigase  
RUN wget 'https://projects.tigase.org/attachments/download/1885/tigase-
server-5.2.3-b3470-dist-max.tar.gz' -O /tmp/tigase-server.tar.gz  
RUN tar -xC /opt -zf /tmp/tigase-server.tar.gz  
RUN mv /opt/tigase-server* /opt/tigase-server  
  
# setup tigase  
ADD tigase.conf /opt/tigase-server/etc/tigase.conf  
ADD init.properties /opt/tigase-server/etc/init.properties  
RUN cd /opt/tigase-server; test -d ./scripts/admin || cp -r
./src/main/groovy/tigase/admin ./scripts/admin  
RUN echo "call TigAddUserPlainPw('admin@tigase.net', '123456');" >>
/opt/tigase-server/database/derby-schema-5-1.sql  
RUN cd /opt/tigase-server; ./scripts/db-create-derby.sh tigasedb; cat derby-
db-create.txt  
  
# run tigase  
CMD cd /opt/tigase-server; java -version; ./scripts/tigase.sh run
etc/tigase.conf; wait $!  
EXPOSE 5222 5223 5269 5270 5290  

