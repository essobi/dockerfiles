# hadoop  
  
FROM takaomag/base:2017.08.07.07.13  
  
ENV \  
X_DOCKER_REPO_NAME=hadoop \  
HADOOP_LOG_DIR=/var/log/hadoop \  
HADOOP_PID_DIR=/run/hadoop \  
# HADOOP_SLAVES=/opt/local/hadoop/etc/hadoop/slaves \  
HADOOP_DFS_NAMENODE_NAME_DIR=file:///var/db/hadoop/dfs/name \  
HADOOP_DFS_NAMENODE_CHECKPOINT_DIR=file:///var/db/hadoop/dfs/namesecondary \  
HADOOP_DFS_DATANODE_DATA_DIR=file:///var/db/hadoop/dfs/data  
  
#ADD files /  
ADD files/etc/supervisor.d/hadoop /etc/supervisor.d/hadoop  
ADD files/opt/local/bin /opt/local/bin  
  
RUN \  
echo "2016-03-08-0" > /dev/null && \  
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
  
chmod 755 /etc/supervisor.d/hadoop && \  
chmod 600 /etc/supervisor.d/hadoop/* && \  
chmod 755 /opt/local/bin/x-start_hdfs-*.sh && \  
echo -e "${FONT_INFO}[INFO] Configure
hadoop-${X_HADOOP_VERSION}${FONT_DEFAULT}" && \  
for _d in $(echo ${HADOOP_DFS_NAMENODE_NAME_DIR} | sed -e 's/,/ /g');do \  
mkdir -p --mode=0755 ${_d:7}; \  
done && \  
for _d in $(echo ${HADOOP_DFS_NAMENODE_CHECKPOINT_DIR} | sed -e 's/,/ /g');do
\  
mkdir -p --mode=0755 ${_d:7}; \  
done && \  
for _d in $(echo ${HADOOP_DFS_DATANODE_DATA_DIR} | sed -e 's/,/ /g');do \  
mkdir -p --mode=0700 ${_d:7}; \  
done && \  
mkdir -p --mode=0755 ${HADOOP_LOG_DIR} && \  
mkdir -p --mode=0744 ${HADOOP_PID_DIR} && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Configure
hadoop-${X_HADOOP_VERSION}${FONT_DEFAULT}" && \  
  
echo -e "${FONT_INFO}[INFO] Configure supervisord${FONT_DEFAULT}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Configure supervisord${FONT_DEFAULT}" && \  
  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  

