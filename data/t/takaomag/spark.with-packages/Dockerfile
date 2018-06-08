# spark.with-packages  
FROM takaomag/spark:release-2.0.2-2017.01.16.05.02  
ENV \  
X_DOCKER_REPO_NAME=spark.with-packages  
  
ADD files /  
  
RUN \  
echo "2016-04-22-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}" &&
\  
pacman-key --refresh-keys && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Test pyspark${FONT_DEFAULT}" && \  
mkdir /tmp/spark-test && \  
cd /tmp/spark-test && \  
/opt/local/spark/bin/spark-submit \  
\--packages 'de.bwaldvogel:log4j-systemd-journal-
appender:1.3.2,org.apache.spark:spark-sql-
kafka-0-10_2.11:2.0.2,org.apache.spark:spark-streaming-
kafka-0-10_2.11:2.0.2,com.amazonaws:aws-java-sdk-
pom:1.11.83,org.apache.hadoop:hadoop-aws:2.7.3,datastax:spark-cassandra-
connector:2.0.0-M2-s_2.11,graphframes:graphframes:0.3.0-spark2.0-s_2.11' \  
\--driver-library-path '/opt/local/hadoop/lib/native' \  
\--conf 'spark.local.dir=/tmp/spark-test' \  
\--conf 'spark.executor.extraLibraryPath=/opt/local/hadoop/lib/native' \  
\--conf 'spark.io.compression.codec=lz4' \  
\--conf 'spark.serializer=org.apache.spark.serializer.KryoSerializer' \  
\--conf
"spark.executor.extraJavaOptions=-Dlog4j.configuration=file:///opt/local/spark/conf/log4j.properties
-Dlog4j.debug=true" \  
\--driver-java-options
"-Dlog4j.configuration=file:///opt/local/spark/conf/log4j.properties
-Dlog4j.debug=true" \  
/tmp/test-spark.py && \  
rm -f /tmp/test-spark.py && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Test pyspark${FONT_DEFAULT}" && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
rm -f /etc/machine-id  
  

