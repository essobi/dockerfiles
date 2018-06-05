# OrientDB  
#  
# VERSION 0.0.1  
#  
# 0.0.1 : initial creation of image for OrientDB  
FROM bibbox/java:latest  
  
MAINTAINER Robert Reihs <robert.reihs@gmail.com>  
  
RUN mkdir /orientdb && \  
wget
"http://orientdb.com/download.php?email=unknown@unknown.com&file=orientdb-
community-2.1.15.tar.gz&os=linux" -O orientdb-community-2.1.15.tar.gz \  
&& tar -xvzf orientdb-community-2.1.15.tar.gz -C /orientdb --strip-
components=1 \  
&& rm orientdb-community-2.1.15.tar.gz \  
&& sed -i 's/YOUR_ORIENTDB_INSTALLATION_PATH/\/orientdb/g'
/orientdb/bin/orientdb.sh \  
&& sed -i 's/USER_YOU_WANT_ORIENTDB_RUN_WITH/root/g' /orientdb/bin/orientdb.sh  
  
CMD ["/orientdb/bin/server.sh"]  

