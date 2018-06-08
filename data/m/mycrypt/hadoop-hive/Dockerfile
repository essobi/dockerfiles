FROM mycrypt/hadoop  
MAINTAINER Bai Xiaoyong lostitle@gmail.com  
  
RUN mkdir /opt/hive  
RUN wget -qO- http://apache.stu.edu.tw/hive/stable/apache-
hive-0.13.1-bin.tar.gz \  
| tar zxvf - -C /opt/hive --strip 1  
  
RUN cp /opt/hive/conf/hive-default.xml.template /opt/hive/conf/hive-
default.xml && \  
cp /opt/hive/conf/hive-default.xml.template /opt/hive/conf/hive-site.xml && \  
cp /opt/hive/conf/hive-env.sh.template /opt/hive/conf/hive-env.sh && \  
cp /opt/hive/conf/hive-log4j.properties.template /opt/hive/conf/hive-
log4j.properties  
  
ENV PATH /opt/hive/bin:$PATH  
  
RUN echo "\n\  
export HIVE_HOME=/opt/hive\n\  
PATH=$HIVE_HOME/bin:$PATH\  
\n\  
" >> /etc/profile

