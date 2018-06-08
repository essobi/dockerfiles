FROM panos/spark  
  
LABEL maintainer "Panayiotis Vlantis <panosv@di.uoa.gr>"  
  
LABEL adam 0.21.1-SNAPSHOT  
  
RUN yum -y install java-1.8.0-openjdk-devel git-core && \  
mkdir maven && \  
curl -s http://www-us.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
| gunzip | tar x --strip=1 -C maven && \  
git clone https://github.com/bigdatagenomics/adam && \  
cd adam && \  
git reset --hard 5ae88202339b47851ab91f85c58a1185ad232740 && \  
scripts/move_to_spark_2.sh && \  
scripts/move_to_scala_2.11.sh && \  
JAVA_HOME=/usr/lib/jvm/java-1.8.0 /opt/maven/bin/mvn clean package -DskipTests
&& \  
mv adam-assembly/target/adam*.jar /opt/adam.jar && \  
cd /opt && \  
rm -rf adam maven /root/.m2 && \  
yum -y autoremove git-core java-1.8.0-openjdk-devel && \  
yum -y clean all  
  
# create entrypoint script  
RUN echo -e '#!/usr/bin/env bash'\\\n'$SPARK_HOME/bin/spark-shell' \  
\--conf spark.serializer=org.apache.spark.serializer.KryoSerializer \  
\--conf
spark.kryo.registrator=org.bdgenomics.adam.serialization.ADAMKryoRegistrator \  
\--jars /opt/adam.jar '$@'> /usr/bin/adam-shell && \  
chmod +x /usr/bin/adam-shell  
  
ADD spark-defaults.conf /opt/spark/conf/  
  
EXPOSE 4040 7077 8080 8181  
ENTRYPOINT ["/usr/bin/adam-shell"]  

