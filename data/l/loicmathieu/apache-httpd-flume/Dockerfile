###########################################################################################  
# This dockerfile is derived from loicmathieu/openjdk and will setup an Apache
2 httd  
# webserver and Apache Flume with an agent configure to collect the apache
access log file  
# and send it to an Hadoop edge node (see loicmathieu/cloudera-cdh-edgenode).  
#  
# The namenode will expose it's 8020 port, to use it, you first need to start
a datanode  
# (using loicmathieu/cloudera-hdfs-datanode) and make sure the netword stack
is OK  
# so that the namenode and datanode can communicate together  
#  
# The container will use supervisor to start both the apache httpd and the
flume agent  
###########################################################################################  
FROM loicmathieu/openjdk  
  
MAINTAINER Loic Mathieu <loicmathieu@free.fr>  
  
#Install epel repo because supervisor isn't in the base repo  
RUN yum -y install epel-release && rm -rf /var/cache/yum/*  
  
#install needed tools wget and supervisor  
RUN yum -y install wget supervisor && yum clean all  
  
#install Apache dependances : APR (Apache Portable Runtime), GCC, make  
#and PCRE (Perl Compatible Regular Expressions)  
RUN yum -y install apr-devel apr-util-devel pcre-devel gcc make && yum clean
all  
  
#Install the Apache httpd webserver : we cannot install it directly with yum
because of the still not  
#solved cap_set_file issue : https://github.com/docker/hub-feedback/issues/543
so I do it manually  
#RUN yum -y install httpd-2.4.20 && rm -rf /var/cache/yum/*  
WORKDIR /tmp  
RUN wget -q http://apache.trisect.eu//httpd/httpd-2.4.20.tar.gz  
RUN tar -xvf httpd-2.4.20.tar.gz  
WORKDIR /tmp/httpd-2.4.20  
RUN ./configure  
RUN make -s && make -s install  
RUN rm -rf /tmp/httpd-2.4.20  
  
#install Apache flume  
WORKDIR /tmp  
RUN wget -q http://apache.crihan.fr/dist/flume/1.6.0/apache-
flume-1.6.0-bin.tar.gz  
RUN tar -xvf apache-flume-1.6.0-bin.tar.gz -C /usr/lib  
RUN rm -rf /tmp/apache-flume-1.6.0-bin.tar.gz  
  
#configure flume  
COPY flume_httpd.conf /usr/lib/apache-flume-1.6.0-bin/conf/flume_httpd.conf  
  
#setup supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#expose httpd port (/usr/local/apache2/htdocs)  
EXPOSE 80  
#start the supervisor  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

