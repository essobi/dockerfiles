FROM mikeford/hbase:latest  
  
# Kylin depends on Hive and Hbase. Since Docker doesn't have multiple image
inheritance, we choose to inherit  
# from Hbase and then manually install Hive (somewhat leaky abstraction).  
# Can probably use multi-stage builds to make this cleaner / only require
downloading tars once.  
ARG HIVE_VERSION=1.2.1  
RUN set -x \  
&& curl -fSL https://archive.apache.org/dist/hive/hive-${HIVE_VERSION}/apache-
hive-${HIVE_VERSION}-bin.tar.gz -o /tmp/hive.tar.gz \  
&& tar -zxvf /tmp/hive.tar.gz -C /usr/local/ \  
&& rm /tmp/hive.tar.gz*  
ENV HIVE_HOME /usr/local/apache-hive-${HIVE_VERSION}-bin  
ADD hive-site.xml $HIVE_HOME/conf  
  
# Install Kylin  
ARG KYLIN_VERSION=2.2.0  
RUN set -x \  
&& curl -fSL http://www-us.apache.org/dist/kylin/apache-
kylin-${KYLIN_VERSION}/apache-kylin-${KYLIN_VERSION}-bin-hbase1x.tar.gz -o
/tmp/kylin.tar.gz \  
&& tar -zxvf /tmp/kylin.tar.gz -C /usr/local/ \  
&& rm /tmp/kylin.tar.gz*  
ENV KYLIN_HOME /usr/local/apache-kylin-${KYLIN_VERSION}-bin  
ADD kylin.properties $KYLIN_HOME/conf  
  
ENV PATH $HADOOP_PREFIX/bin:$HIVE_HOME/bin:$HBASE_HOME/bin:$PATH  
  
ADD wait-for-it.sh /wait-for-it.sh  
RUN chmod a+x /wait-for-it.sh  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
CMD ["/run.sh"]  

