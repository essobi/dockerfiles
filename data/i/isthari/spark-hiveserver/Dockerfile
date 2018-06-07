FROM isthari/spark-base:latest  
  
ENV JAVA_HOME /usr  
  
EXPOSE 10000  
CMD cd root; ./spark/bin/spark-submit --class
org.apache.spark.sql.hive.thriftserver.HiveThriftServer2 --master $MASTER
$OPTIONS \--conf spark.sql.warehouse.dir=hdfs://hdfs-
namenode:8020/user/hive/warehouse  
  

