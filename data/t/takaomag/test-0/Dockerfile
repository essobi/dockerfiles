# spark  
# - build with netlib-java  
# http://qiita.com/adachij2002/items/b9af506d704434f4f293  
  
FROM quay.io/takaomag/netlib-java:release-1.1.2-2018.03.10.05.27  
  
ENV \  
X_DOCKER_REPO_NAME=spark \  
X_SPARK_VERSION=2.3.0 \  
SPARK_HOME=/opt/local/spark \  
PYSPARK_DRIVER_PYTHON=/opt/local/python-3/bin/python3 \  
PYSPARK_PYTHON=/opt/local/python-3/bin/python3 \  
#
SPARK_EXECUTOR_URI=file:///opt/local/spark/dist/spark-2.3.0-bin-${X_HADOOP_VERSION}.tgz
\  
SPARK_EXECUTOR_URI=file:///opt/local/spark/dist/spark-2.3.0-bin-2.9.0.tgz \  
X_HADOOP_VERSION=3.0.0 \  
LD_LIBRARY_PATH=/usr/lib/hadoop/lib/native:$LD_LIBRARY_PATH \  
HADOOP_HOME=/usr/lib/hadoop \  
HADOOP_PREFIX=/usr/lib/hadoop \  
HADOOP_COMMON_HOME=/usr/lib/hadoop \  
HADOOP_HDFS_HOME=/usr/lib/hadoop \  
HADOOP_YARN_HOME=/usr/lib/hadoop \  
HADOOP_MAPRED_HOME=/usr/lib/hadoop \  
HADOOP_COMMON_LIB_NATIVE_DIR=/usr/lib/hadoop/lib/native \  
HADOOP_CONF_DIR=/etc/hadoop \  
YARN_CONF_DIR=/etc/hadoop \  
HADOOP_USER_NAME=hadoop \  
HADOOP_OPTS="-Djava.library.path=/usr/lib/hadoop/lib/native" \  
HADOOP_LOG_DIR=/var/log/hadoop \  
HADOOP_PID_DIR=/run/hadoop \  
# HADOOP_SLAVES=/etc/hadoop/slaves \  
HADOOP_DFS_NAMENODE_NAME_DIR=file:///var/db/hadoop/dfs/name \  
HADOOP_DFS_NAMENODE_CHECKPOINT_DIR=file:///var/db/hadoop/dfs/namesecondary \  
HADOOP_DFS_DATANODE_DATA_DIR=file:///var/db/hadoop/dfs/data  
  
# X_SPARK_VERSION=2.1.0-rc5 \  
# X_SPARK_CLONE_REPO_CMD="git clone -b branch-2.0
git://git.apache.org/spark.git" \  
#
X_SPARK_DOWNLOAD_URI="https://github.com/apache/spark/archive/v2.1.0-rc5.tar.gz"
\  
#
X_SPARK_DOWNLOAD_URI="http://ftp.riken.jp/net/apache/spark/spark-2.0.1/spark-2.0.1.tgz"
\  
# HADOOP_HOME=/opt/local/hadoop \  
# HADOOP_PREFIX=/opt/local/hadoop \  
# HADOOP_COMMON_HOME=/opt/local/hadoop \  
# HADOOP_COMMON_LIB_NATIVE_DIR=/opt/local/hadoop/lib/native \  
# HADOOP_HDFS_HOME=/opt/local/hadoop \  
# HADOOP_MAPRED_HOME=/opt/local/hadoop \  
# HADOOP_YARN_HOME=/opt/local/hadoop \  
# HADOOP_CONF_DIR=/opt/local/hadoop/etc/hadoop \  
# YARN_CONF_DIR=/opt/local/hadoop/etc/hadoop \  
# HADOOP_USER_NAME=root \  
# HADOOP_OPTS="-Djava.library.path=/opt/local/hadoop/lib/native" \  
# PATH=/opt/local/hadoop/sbin:/opt/local/hadoop/bin:${PATH} \  
  
RUN \  
echo "2016-05-06-1" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
: && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u x-aur-helper yay -Syy --noprogressbar && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
: && \  
# echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}"
&& \  
# pacman-key --refresh-keys && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
#: && \  
# required by mesos native library  
# pandoc is required to avoid the message "Could not import pypandoc -
required to package PySpark See
http://johnmacfarlane.net/pandoc/installing.html for installation options".  
# REQUIRED_PACKAGES=("boost" "gperftools" "google-glog" "leveldb" "protobuf"
"protobuf-java" "picojson-git") && \  
REQUIRED_PACKAGES=("pandoc" "hadoop" "gperftools" "google-glog" "leveldb"
"protobuf" "picojson-git") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u x-aur-helper yay -S --needed --noconfirm --noprogressbar
${REQUIRED_PACKAGES[@]} && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
/opt/local/python-3/bin/pip3 install -U pypandoc && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install hadoop-${X_HADOOP_VERSION}${FONT_DEFAULT}"
&& \  
for _d in $(echo ${HADOOP_DFS_NAMENODE_NAME_DIR} | sed -e 's/,/ /g');do \  
mkdir -p --mode=0755 ${_d:7} && \  
chown hadoop:hadoop ${_d:7}; \  
done && \  
for _d in $(echo ${HADOOP_DFS_NAMENODE_CHECKPOINT_DIR} | sed -e 's/,/ /g');do
\  
mkdir -p --mode=0755 ${_d:7} && \  
chown hadoop:hadoop ${_d:7}; \  
done && \  
for _d in $(echo ${HADOOP_DFS_DATANODE_DATA_DIR} | sed -e 's/,/ /g');do \  
mkdir -p --mode=0700 ${_d:7} && \  
chown hadoop:hadoop ${_d:7}; \  
done && \  
mkdir -p --mode=0755 ${HADOOP_LOG_DIR} && \  
chown hadoop:hadoop ${HADOOP_LOG_DIR} && \  
mkdir -p --mode=0744 ${HADOOP_PID_DIR} && \  
chown hadoop:hadoop ${HADOOP_PID_DIR} && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
hadoop-${X_HADOOP_VERSION}${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install spark-${X_SPARK_VERSION}${FONT_DEFAULT}"
&& \  
archlinux-java set java-8-openjdk && \  
([ -d /opt/local ] || mkdir -p /opt/local) && \  
cd /var/tmp && \  
if [[ "${X_SPARK_CLONE_REPO_CMD}" ]];then\  
${X_SPARK_CLONE_REPO_CMD} && mv spark spark-${X_SPARK_VERSION};\  
elif [[ "${X_SPARK_DOWNLOAD_URI}" ]];then\  
curl --silent --location --fail --retry 5 "${X_SPARK_DOWNLOAD_URI}" | tar xz;\  
else\  
APACHE_CLOSER_MIRROR=$(curl --silent --location --fail --retry 5 --stderr
/dev/null "https://www.apache.org/dyn/closer.cgi?as_json=1" | jq -r
'.preferred') && \  
curl --silent --location --fail --retry 5
"${APACHE_CLOSER_MIRROR}spark/spark-${X_SPARK_VERSION}/spark-${X_SPARK_VERSION}.tgz"
| tar xz;\  
fi && \  
cd spark-${X_SPARK_VERSION} && \  
if [[ "${X_SPARK_VERSION}" == '2.1.0' ]];then\  
# https://github.com/apache/spark/pull/16429  
rm -f python/pyspark/cloudpickle.py && \  
curl --silent --location --fail --retry 5 -o python/pyspark/cloudpickle.py
"https://raw.githubusercontent.com/HyukjinKwon/spark/6458d4185da9ed9772bb4317a82b26da784a89ee/python/pyspark/cloudpickle.py"
&& \  
rm -f python/pyspark/serializers.py && \  
curl --silent --location --fail --retry 5 -o python/pyspark/serializers.py
"https://raw.githubusercontent.com/HyukjinKwon/spark/6458d4185da9ed9772bb4317a82b26da784a89ee/python/pyspark/serializers.py";\  
fi && \  
# Hive does not support hadoop 3.0.0 yet  
X_HADOOP_VERSION=2.9.0 && \  
# [[ "$(cut -d. -f1 <<< ${X_HADOOP_VERSION})" != '3' ]] || sed --in-place -e
's|<id>hadoop-2\\.7</id>|<id>hadoop-3\\.0</id>|g' -e
's|<hadoop\\.version>2\\.7\\.3</hadoop\\.version>|<hadoop\\.version>3\\.0\\.0</hadoop\\.version>|g'
pom.xml && \  
cp -ap conf/log4j.properties.template conf/org.log4j.properties.template && \  
sed --in-place -e 's|log4j\\.rootCategory=INFO|log4j\\.rootCategory=WARN|g' -e
's|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkIMain$exprTyper=INFO|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkIMain$exprTyper=WARN|g'
-e
's|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkILoop$SparkILoopInterpreter=INFO|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkILoop$SparkILoopInterpreter=WARN|g'
conf/log4j.properties.template && \  
X_WITH_NETLIB='-Pnetlib-lgpl' && \  
export X_INTERNAL_SPARK_VERSION=$(build/mvn help:evaluate
-Dexpression=project.version 2>/dev/null | egrep -v -e '^\\[.+\\]' | tail -n
1) && \  
X_INTERNAL_SPARK_VERSION_MAJOR=$(cut -d '.' -f 1 <<<
${X_INTERNAL_SPARK_VERSION}) && \  
[[ -f ./make-distribution.sh ]] && MAKE_DIST_PATH='./make-distribution.sh' ||
MAKE_DIST_PATH='dev/make-distribution.sh' && \  
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk && \  
export MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=512m" && \  
if [[ ${X_INTERNAL_SPARK_VERSION_MAJOR} -ge 2 ]];then\  
${MAKE_DIST_PATH} \--tgz -Pyarn -Phadoop-2.7
-Dhadoop.version=${X_HADOOP_VERSION} -Phive -Phive-thriftserver -Pmesos
-Pkubernetes ${X_WITH_NETLIB};\  
else\  
${MAKE_DIST_PATH} \--tgz --skip-java-test --with-tachyon -Pyarn -Phadoop-2.7
-Dhadoop.version=${X_HADOOP_VERSION} -Phive -Phive-thriftserver
${X_WITH_NETLIB};\  
fi && \  
cp -ap dist/conf/log4j.properties.template dist/conf/log4j.properties && \  
mkdir x_mago_dist && \  
tar xvzf spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}.tgz -C
x_mago_dist/. && \  
rm spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}.tgz && \  
# cp /tmp/log4j-systemd-journal-appender-1.3.2.jar
x_mago_dist/spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}/jars/.
&& \  
cp /usr/share/java/jna.jar
x_mago_dist/spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}/jars/.
&& \  
cp -ap
x_mago_dist/spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}/conf/log4j.properties.template
x_mago_dist/spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}/conf/log4j.properties
&& \  
cd
x_mago_dist/spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}/python
&& \  
/opt/local/python-3/bin/python3 setup.py sdist && \  
/opt/local/python-3/bin/python3 setup.py bdist_wheel && \  
rm -rf build/ .eggs/ pyspark.egg-info/ && \  
cd ../../.. && \  
tar -C x_mago_dist -czf
spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION}.tgz
spark-${X_INTERNAL_SPARK_VERSION}-bin-${X_HADOOP_VERSION} && \  
rm -rf x_mago_dist && \  
cd dist/python && \  
/opt/local/python-3/bin/python3 setup.py sdist && \  
/opt/local/python-3/bin/python3 setup.py bdist_wheel && \  
rm -rf build/ .eggs/ pyspark.egg-info/ && \  
cd ../.. && \  
porg --log \--package="spark-${X_SPARK_VERSION}" \-- mv dist
/opt/local/spark-${X_SPARK_VERSION} && \  
porg --log \--package="spark-${X_SPARK_VERSION}" -+ -- mkdir
/opt/local/spark-${X_SPARK_VERSION}/dist && \  
porg --log \--package="spark-${X_SPARK_VERSION}" -+ -- mv
spark-${X_INTERNAL_SPARK_VERSION}*.tgz
/opt/local/spark-${X_SPARK_VERSION}/dist/. && \  
cd /opt/local && \  
porg --log \--package="spark-${X_SPARK_VERSION}" -+ -- ln -sf
spark-${X_SPARK_VERSION} spark && \  
# porg --log --package="spark-${X_SPARK_VERSION}" -+ -- mv /tmp/log4j-systemd-
journal-appender-1.3.2.jar spark-${X_SPARK_VERSION}/jars/. && \  
porg --log \--package="spark-${X_SPARK_VERSION}" -+ -- cp
/usr/share/java/jna.jar spark-${X_SPARK_VERSION}/jars/. && \  
rm -rf /var/tmp/spark-${X_SPARK_VERSION} && \  
# /opt/local/python-3/bin/pip3 install -U
/opt/local/spark/python/dist/*.tar.gz && \  
/opt/local/python-3/bin/pip3 install -U /opt/local/spark/python/dist/*.whl &&
\  
archlinux-java set java-9-openjdk && \  
rm -rf /root/.m2/repository && \  
rm -rf /root/.ivy2/cache && \  
rm -rf /root/.gradle/caches && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
spark-${X_SPARK_VERSION}${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
# spark.mesos.executor.docker.image assumes the default working directory of
the container to be inside $SPARK_HOME.  
WORKDIR /opt/local/spark  
  
# mvn -Pyarn -Phadoop-2.4 -Dhadoop.version=2.6.0 -Phive -Phive-thriftserver
-DskipTests clean package && \  
# envs  
# SPARK_HOME  
# SPARK_CONF_DIR  
# PYSPARK_PYTHON  
# PYSPARK_DRIVER_PYTHON  
# SPARKR_DRIVER_R  
# SPARK_LOCAL_IP  
# SPARK_PUBLIC_DNS  
# SPARK_LOCAL_DIRS (standalone or mesos)  
# LOCAL_DIRS (yarn)  
# SPARK_EXECUTOR_URK (for mesos)  

