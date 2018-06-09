FROM nerdammer/hbase:1.1.0.1  
MAINTAINER ivan Bettarini <ivan.bettarini@gmail.com>  
  
RUN curl 'https://bootstrap.pypa.io/get-pip.py' > get-pip.py  
RUN python get-pip.py  
RUN pip install supervisor  
  
ADD hbase-site.xml /opt/hbase/conf/hbase-site.xml  
ADD start-pseudo-distributed-thrift.sh /opt/hbase/bin/start-pseudo-
distributed-thrift.sh  
ADD supervisor.conf /opt/hbase/supervisor.conf  
  
RUN chmod +x /opt/hbase/bin/start-pseudo-distributed-thrift.sh  
RUN mkdir /opt/hbase/bin/initial_script  
VOLUME /opt/hbase/bin/initial_script  
  
# rest server  
EXPOSE 8080  
# thtift server  
EXPOSE 9090  
# supervisor server  
EXPOSE 9001  
EXPOSE 12345  
CMD /opt/hbase/bin/start-pseudo-distributed-thrift.sh  

