FROM fayehuang/centos-supervisor  
MAINTAINER FayeHuang  
  
WORKDIR /root  
ENV dockerENV /etc/profile.d/dockerEnv.sh  
RUN touch $dockerENV  
  
# flume 1.6 download : https://flume.apache.org/download.html  
RUN yum install -y wget tar && yum clean all  
RUN wget http://apache.stu.edu.tw/flume/1.6.0/apache-flume-1.6.0-bin.tar.gz  
RUN tar zxvf apache-flume-1.6.0-bin.tar.gz && rm -f apache-
flume-1.6.0-bin.tar.gz  
RUN mv apache-flume-1.6.0-bin flume  
ENV FLUME_HOME=/root/flume  
RUN echo "export FLUME_HOME=$FLUME_HOME" >> $dockerENV  
  
# openjdk 1.7 install  
RUN yum install -y java-1.7.0-openjdk java-1.7.0-openjdk-devel && yum clean
all  
ENV JAVA_HOME=/usr/lib/jvm/jre-1.7.0-openjdk.x86_64  
RUN echo "export JAVA_HOME=$JAVA_HOME" >> $dockerENV  
  
# ant 1.9.5 download : http://ant.apache.org/bindownload.cgi  
RUN wget http://ftp.twaren.net/Unix/Web/apache//ant/binaries/apache-
ant-1.9.5-bin.tar.gz  
RUN tar zxvf apache-ant-1.9.5-bin.tar.gz && rm -f apache-ant-1.9.5-bin.tar.gz  
RUN mv apache-ant-1.9.5 ant  
ENV ANT_HOME=/root/ant  
RUN echo "export ANT_HOME=$ANT_HOME" >> $dockerENV  
  
# set PATH  
RUN echo "export PATH=$ANT_HOME/bin:$JAVA_HOME/bin:$FLUME_HOME/bin:$PATH" >>
$dockerENV  
  
# build SplittingSerializer (flume AsyncHbaseEventSerializer)  
ENV HBASE_SER_HOME=/root/SplittingSerializer  
COPY SplittingSerializer $HBASE_SER_HOME  
RUN $ANT_HOME/bin/ant -file $HBASE_SER_HOME/build.xml clean  
RUN $ANT_HOME/bin/ant -file $HBASE_SER_HOME/build.xml jar  
RUN cp $HBASE_SER_HOME/build/jar/SplittingSerializer.jar $FLUME_HOME/lib/  
  
# start flume agent  
RUN mv $FLUME_HOME/conf/flume-conf.properties.template $FLUME_HOME/conf/flume-
conf.properties  
RUN mv $FLUME_HOME/conf/flume-env.sh.template $FLUME_HOME/conf/flume-env.sh  
  
# TODO : install hadoop, hbase client(HDP,CDH)  
# (1) setting yum repository  
# (2) yum install hadoop hbase  
# (3) setting cluster hostname IP mapping  
# (4) copy client conf  
COPY cloudera-cdh5.repo /etc/yum.repos.d/cloudera-cdh5.repo  
#COPY hdp.repo /etc/yum.repos.d/hdp.repo  
RUN yum install -y hadoop hbase && yum clean all  
  
#  
EXPOSE 22  
COPY supervisord.conf /etc/supervisord.conf  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

