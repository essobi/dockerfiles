FROM openjdk:9.0.1-11-jre-sid  
  
ARG HADOOP_VERSION="3.0.0"  
ARG HADOOP_BASE="/opt"  
ARG HADOOP_FULLNAME="hadoop-${HADOOP_VERSION}"  
ARG
HADOOP_DOWNLOAD_URL="http://apache.claz.org/hadoop/common/${HADOOP_FULLNAME}/${HADOOP_FULLNAME}.tar.gz"  
ARG HADOOP_UID=1000  
ARG HADOOP_GID=1000  
ENV HADOOP_HOME="/opt/hadoop" \  
HADOOP_PID_DIR="/var/run/hadoop" \  
HADOOP_LOG_DIR="/var/log/hadoop" \  
HADOOP_USER="hadoop" \  
HADOOP_CONFIG_DIR="/etc/hadoop" \  
HADOOP_DATA_DIR="/var/lib/hadoop" \  
HADOOP_CONFIG_TEMP_DIR="/config_template"  
ENV HADOOP_NAMENODE_URI="hdfs://localhost"  
ENV JAVA_HEAPSIZE="1g" \  
JAVA_GC_OPTS="-XX:+UseG1GC" \  
JAVA_GC_LOG_OPTS=""  
ENV SCRIPTS_DIR="/scripts" \  
USER_ADDITION_SCRIPTS_DIR="/user_addition_scripts" \  
ROOT_ADDITION_SCRIPTS_DIR="/root_addition_scripts"  
ARG SU_EXEC_VERSION=0.2  
ARG SU_EXEC_URL="https://github.com/ncopa/su-
exec/archive/v${SU_EXEC_VERSION}.tar.gz"  
RUN apt-get update && apt-get -y install gcc make \  
&& curl -sL "${SU_EXEC_URL}" | tar -C /tmp -zx \  
&& make -C "/tmp/su-exec-${SU_EXEC_VERSION}" \  
&& cp "/tmp/su-exec-${SU_EXEC_VERSION}/su-exec" /usr/bin \  
&& rm -fr "/tmp/su-exec-${SU_EXEC_VERSION}" \  
&& groupadd -g "${HADOOP_GID}" -r "${HADOOP_USER}" \  
&& useradd -g "${HADOOP_USER}" -u "${HADOOP_UID}" -d "${HADOOP_HOME}" -M -r -s
"/bin/bash" "${HADOOP_USER}" \  
&& mkdir -p "${HADOOP_BASE}" \  
&& curl -L "${HADOOP_DOWNLOAD_URL}" | tar -C "${HADOOP_BASE}" \--no-same-owner
-xzf - \  
&& ln -snf "${HADOOP_BASE}/${HADOOP_FULLNAME}" "${HADOOP_HOME}" \  
&& rm -fr "${HADOOP_HOME}/include" "${HADOOP_HOME}/lib/native/examples" \  
"${HADOOP_HOME}/share/doc" \  
&& find "${HADOOP_HOME}/share/hadoop" -name sources -type d -prune -exec rm
-fr {} \; \  
&& find "${HADOOP_HOME}/share/hadoop" -name templates -type d -prune -exec rm
-fr {} \; \  
&& find "${HADOOP_HOME}/share/hadoop" -name jdiff -type d -prune -exec rm -fr
{} \; \  
&& find "${HADOOP_HOME}/share/hadoop" -name test -type d -prune -exec rm -fr
{} \; \  
&& find "${HADOOP_HOME}/share/hadoop" -name "lib-examples" -type d -prune
-exec rm -fr {} \; \  
&& find "${HADOOP_HOME}/share/hadoop" -name "*-tests.jar" -type f -exec rm -f
{} \; \  
&& mv "${HADOOP_HOME}/etc" /hadoop_etc_orig \  
&& mkdir -p "${HADOOP_CONFIG_TEMP_DIR}" "${SCRIPTS_DIR}" \  
&& mkdir -p "${HADOOP_PID_DIR}" "${HADOOP_DATA_DIR}" "${HADOOP_CONFIG_DIR}"
"${HADOOP_LOG_DIR}" \  
&& chown -R "${HADOOP_USER}:${HADOOP_USER}" "${HADOOP_PID_DIR}"
"${HADOOP_DATA_DIR}" "${HADOOP_LOG_DIR}" \  
&& mkdir -p /scripts "${USER_ADDITION_SCRIPTS_DIR}"
"${ROOT_ADDITION_SCRIPTS_DIR}" \  
&& apt-get -y autoremove --purge gcc make \  
&& apt-get -y clean \  
&& rm -fr /var/lib/apt/lists/*  
  
ADD docker-entrypoint.sh "${SCRIPTS_DIR}"  
ADD core-site.xml.tmpl "${HADOOP_CONFIG_TEMP_DIR}"  
  
VOLUME "${HADOOP_DATA_DIR}" "${HADOOP_LOG_DIR}"  
  
WORKDIR "${HADOOP_HOME}"  
  
ENTRYPOINT [ "/scripts/docker-entrypoint.sh" ]  

