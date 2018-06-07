FROM cassandra:3.9  
RUN apt-get update && apt-get install -y wget  
RUN wget https://raw.githubusercontent.com/docker-
library/cassandra/3ca0a18a575ae318f753ab1ecf01d54c93192681/3.9/docker-
entrypoint.sh -O docker-entrypoint-cassandra.sh  
RUN chmod +x docker-entrypoint-cassandra.sh  
RUN wget
http://mirrors.whoishostingthis.com/apache/spark/spark-2.1.0/spark-2.1.0-bin-
hadoop2.7.tgz -P /opt/  
RUN tar xfz /opt/spark-2.1.0-bin-hadoop2.7.tgz -C /opt  
RUN ln -s /opt/spark-2.1.0-bin-hadoop2.7 /opt/spark-latest  
COPY ./spark-conf/* /opt/spark-latest/conf/  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
RUN rm /opt/*gz  
EXPOSE 8080 7077 22222 45000-55000 7000 7001 7199 9042 9160 8080 7077 22222  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["cassandra","-f"]  
  

