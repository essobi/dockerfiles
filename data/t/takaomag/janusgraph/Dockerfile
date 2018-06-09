# JanusGraph  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=janusgraph \  
# X_JANUSGRAPH_VERSION=0.2.0 \  
X_JANUSGRAPH_GIT_URL=https://github.com/JanusGraph/janusgraph.git \  
# X_JANUSGRAPH_GIT_URL=https://github.com/sjudeng/janusgraph.git \  
X_CASSANDRA_DRIVER_VERSION=3.3.2 \  
X_JANUSGRAPH_GIT_CHECKOUT=master  
# X_JANUSGRAPH_GIT_CHECKOUT=tp33 \  
RUN \  
echo "2016-03-08-0" > /dev/null && \  
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
: `# echo -e "${FONT_INFO}[INFO] Refresh package developer
keys${FONT_DEFAULT}" ` && \  
: `# pacman-key --refresh-keys ` && \  
: `# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" ` && \  
: && \  
REQUIRED_PACKAGES=("jdk8-openjdk") && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install
janusgraph-${X_JANUSGRAPH_VERSION}${X_JANUSGRAPH_GIT_CHECKOUT}${FONT_DEFAULT}"
&& \  
archlinux-java set java-8-openjdk && \  
cd /var/tmp && \  
if [[ "${X_JANUSGRAPH_VERSION}" ]];then\  
curl --silent --location --fail --retry 5
"https://github.com/JanusGraph/janusgraph/releases/download/v${X_JANUSGRAPH_VERSION}/janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2.zip"
| bsdtar -xf- -C /var/tmp && \  
chmod +x janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/bin/*; \  
elif [[ "${X_JANUSGRAPH_GIT_CHECKOUT}" ]];then\  
git clone -b ${X_JANUSGRAPH_GIT_CHECKOUT} ${X_JANUSGRAPH_GIT_URL} && \  
cd janusgraph && \  
mvn clean install -Pjanusgraph-release -Dgpg.skip=true -DskipTests=true
-Dtest.skip.tp=true && \  
cd /var/tmp && \  
X_JANUSGRAPH_VERSION=$(basename $(ls -A janusgraph/janusgraph-dist/janusgraph-
dist-hadoop-2/target/janusgraph-*.zip | head -n1) '.zip' | cut -d '-' -f 2- |
sed -e 's|-hadoop2||') && \  
unzip janusgraph/janusgraph-dist/janusgraph-dist-
hadoop-2/target/janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2.zip && \  
mkdir -p janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/doc && \  
mv janusgraph/janusgraph-dist/target/docs/{chunk,single}
janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/doc/.; \  
else\  
echo -e "${FONT_ERROR}[ERROR] Either X_JANUSGRAPH_VERSION or
X_JANUSGRAPH_GIT_CHECKOUT MUST be specified.${FONT_DEFAULT}" 1>&2 && \  
exit 1; \  
fi && \  
X_GREMLIN_VERSION=$(janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/bin/gremlin.sh
-v 2>/dev/null | egrep -o "Apache TinkerPop [^ ]+" | cut -d ' ' -f3) && \  
LD_LIBRARY_PATH=${HADOOP_COMMON_LIB_NATIVE_DIR}
janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/bin/gremlin-server.sh -i
com.datastax.cassandra cassandra-driver-core ${X_CASSANDRA_DRIVER_VERSION} &&
\  
janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/bin/gremlin-server.sh -i
org.apache.tinkerpop gremlin-python ${X_GREMLIN_VERSION} && \  
rm -rf janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/log && \  
porg --log \--package="janusgraph-${X_JANUSGRAPH_VERSION}" \-- mv
janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2 /opt/local/. && \  
porg --log \--package="janusgraph-${X_JANUSGRAPH_VERSION}" -+ -- ln -sf
/opt/local/janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2 /opt/local/janusgraph &&
\  
porg --log \--package="janusgraph-${X_JANUSGRAPH_VERSION}" -+ -- mkdir
/var/log/janusgraph && \  
porg --log \--package="janusgraph-${X_JANUSGRAPH_VERSION}" -+ -- ln -sf
/var/log/janusgraph /opt/local/janusgraph-${X_JANUSGRAPH_VERSION}-hadoop2/log
&& \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
janusgraph-${X_JANUSGRAPH_VERSION}${FONT_DEFAULT}" && \  
: && \  
: `# REQUIRED_PYTHON_MODULES=("gremlinpython" "aiogremlin" "goblin") ` && \  
# REQUIRED_PYTHON_MODULES=("gremlinpython") && \  
# echo -e "${FONT_INFO}[INFO] Install required python packages
[${REQUIRED_PYTHON_MODULES[@]}]${FONT_DEFAULT}" && \  
# /opt/local/python-3/bin/pip3 install --upgrade
"${REQUIRED_PYTHON_MODULES[@]}" && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PYTHON_MODULES[@]}]${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
: `# pacman-optimize && ` \  
rm -f /etc/machine-id  
  
ADD log4j-systemd-journal-appender-1.3.2.log4j-1.2.16.jna-4.0.0.jar
/opt/local/janusgraph/lib/log4j-systemd-journal-appender-1.3.2.jar  
  
VOLUME ["/var/log/janusgraph"]  
  
WORKDIR /opt/local/janusgraph  
  
EXPOSE \  
8182  

