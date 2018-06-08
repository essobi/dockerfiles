# spark  
# - build with netlib-java  
# http://qiita.com/adachij2002/items/b9af506d704434f4f293  
# FROM takaomag/openblas:release-0.2.20-2017.10.02.01.36  
FROM takaomag/netlib-java:release-1.1.2-2017.12.18.09.45  
  
ENV \  
X_DOCKER_REPO_NAME=spark \  
X_SPARK_VERSION=2.2.1 \  
SPARK_HOME=/opt/local/spark \  
PYSPARK_DRIVER_PYTHON=/opt/local/python-3/bin/python3 \  
PYSPARK_PYTHON=/opt/local/python-3/bin/python3 \  
#
SPARK_EXECUTOR_URI=file:///opt/local/spark/dist/spark-2.2.1-bin-${X_HADOOP_VERSION}.tgz  
SPARK_EXECUTOR_URI=file:///opt/local/spark/dist/spark-2.2.1-bin-2.9.0.tgz  
  
# X_SPARK_VERSION=2.1.0-rc5 \  
# X_SPARK_CLONE_REPO_CMD="git clone -b branch-2.0
git://git.apache.org/spark.git" \  
#
X_SPARK_DOWNLOAD_URI="https://github.com/apache/spark/archive/v2.1.0-rc5.tar.gz"
\  
#
X_SPARK_DOWNLOAD_URI="http://ftp.riken.jp/net/apache/spark/spark-2.0.1/spark-2.0.1.tgz"
\  
  
ADD log4j-systemd-journal-appender-1.3.2.log4j-1.2.17.jna-4.4.0.jar
/tmp/log4j-systemd-journal-appender-1.3.2.jar  
  
RUN \  
echo "2016-05-06-1" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
: && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
: && \  
# echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}"
&& \  
# pacman-key --refresh-keys && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
: && \  
# required by mesos native library  
# REQUIRED_PACKAGES=("boost" "gperftools" "google-glog" "leveldb" "protobuf"
"protobuf-java" "picojson-git") && \  
REQUIRED_PACKAGES=("gperftools" "google-glog" "leveldb" "protobuf" "picojson-
git") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
mkdir /.m2 && \  
chown nobody:nobody /.m2 && \  
cd /var/tmp && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
rm -rf /.m2 && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
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
sed --in-place -e 's|log4j\\.rootCategory=INFO|log4j\\.rootCategory=WARN|g' -e
's|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkIMain$exprTyper=INFO|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkIMain$exprTyper=WARN|g'
-e
's|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkILoop$SparkILoopInterpreter=INFO|log4j\\.logger\\.org\\.apache\\.spark\\.repl\\.SparkILoop$SparkILoopInterpreter=WARN|g'
conf/log4j.properties.template && \  
X_WITH_NETLIB='-Pnetlib-lgpl' && \  
# export X_INTERNAL_SPARK_VERSION=$(build/mvn help:evaluate
-Dexpression=project.version -Pyarn -Phadoop-$(cut -d. -f1,2 <<<
${X_HADOOP_VERSION}) -Dhadoop.version=${X_HADOOP_VERSION} -Phive -Phive-
thriftserver ${X_WITH_NETLIB} 2>/dev/null | egrep -v -e '^\\[.+\\]' | tail -n
1) && \  
export X_INTERNAL_SPARK_VERSION=$(build/mvn help:evaluate
-Dexpression=project.version -Pyarn -Phadoop-2.7
-Dhadoop.version=${X_HADOOP_VERSION} -Phive -Phive-thriftserver
${X_WITH_NETLIB} 2>/dev/null | egrep -v -e '^\\[.+\\]' | tail -n 1) && \  
X_INTERNAL_SPARK_VERSION_MAJOR=$(cut -d '.' -f 1 <<<
${X_INTERNAL_SPARK_VERSION}) && \  
[[ -f ./make-distribution.sh ]] && MAKE_DIST_PATH='./make-distribution.sh' ||
MAKE_DIST_PATH='dev/make-distribution.sh' && \  
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk && \  
# export MAVEN_OPTS="-Xmx2g -XX:MaxPermSize=512M
-XX:ReservedCodeCacheSize=512m" && \  
export MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=512m" && \  
if [[ ${X_INTERNAL_SPARK_VERSION_MAJOR} -ge 2 ]];then\  
${MAKE_DIST_PATH} \--tgz -Pyarn -Phadoop-2.7
-Dhadoop.version=${X_HADOOP_VERSION} -Phive -Phive-thriftserver -Pmesos
${X_WITH_NETLIB};\  
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
cp /tmp/log4j-systemd-journal-appender-1.3.2.jar
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
porg --log \--package="spark-${X_SPARK_VERSION}" -+ -- mv /tmp/log4j-systemd-
journal-appender-1.3.2.jar spark-${X_SPARK_VERSION}/jars/. && \  
porg --log \--package="spark-${X_SPARK_VERSION}" -+ -- cp
/usr/share/java/jna.jar spark-${X_SPARK_VERSION}/jars/. && \  
rm -rf /var/tmp/spark-${X_SPARK_VERSION} && \  
# /opt/local/python-3/bin/pip3 install -U
/opt/local/spark/python/dist/*.tar.gz && \  
/opt/local/python-3/bin/pip3 install -U /opt/local/spark/python/dist/*.whl &&
\  
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

