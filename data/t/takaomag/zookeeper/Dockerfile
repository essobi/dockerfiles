# zookeeper  
# See  
# https://github.com/signalfuse/docker-zookeeper  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=zookeeper \  
X_ZOOKEEPER_VERSION=3.4.11  
#ADD files /  
ADD files/opt/local/bin /opt/local/bin  
  
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
# echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}"
&& \  
# pacman-key --refresh-keys && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
: && \  
REQUIRED_PACKAGES=("zookeeper") && \  
: && \  
archlinux-java set java-9-openjdk && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
_ZOOKEERPER_VERSION=$(sudo -u nobody yaourt -Qe zookeeper 2>/dev/null | cut -d
' ' -f 2 | cut -d '-' -f 1) && \  
# sed --in-place -e "s/^\\(dataDir=.\\+\\)/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #\1/g" /etc/zookeeper/zoo.cfg && \  
sed --in-place -e "s|^\\(maxClientCnxns=.\\+\\)|#
${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} #\1|g" /etc/zookeeper/zoo.cfg && \  
echo -e "\n# ${X_DOCKER_ID}/${X_DOCKER_REPO_NAME}
>>>\nmaxClientCnxns=0\nautopurge.snapRetainCount=3\nautopurge.purgeInterval=1\n#
${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} <<<\n" >> /etc/zookeeper/zoo.cfg && \  
cp -apr /etc/zookeeper/log4j.properties
/etc/zookeeper/.log4j.properties_original && \  
sed --in-place -e "s|^\\(log4j\\.appender\\.ROLLINGFILE.\\+\\)|#
${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} #\1|g" /etc/zookeeper/log4j.properties &&
\  
sed --in-place -e "s|^\\(log4j\\.appender\\.TRACEFILE.\\+\\)|#
${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} #\1|g" /etc/zookeeper/log4j.properties &&
\  
mkdir -p /var/{lib,log}/zookeeper && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install zookeeper-${_ZOOKEERPER_VERSION}
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
ADD log4j-systemd-journal-appender-1.3.2.log4j-1.2.17.jna-4.4.0.jar
/usr/share/java/zookeeper/log4j-systemd-journal-appender-1.3.2.jar  
  
EXPOSE \  
2181 \  
2888 \  
3888  
ENTRYPOINT ["/opt/local/bin/x-start_zookeeper.sh"]  
  
CMD ["-Dlog4j.configuration=file:/etc/zookeeper/log4j.properties",
"-Dzookeeper.log.dir=/var/log/zookeeper",
"-Dzookeeper.root.logger=INFO,CONSOLE", "-Dzookeeper.log.threshold=INFO",
"-Dcom.sun.management.jmxremote",
"-Dcom.sun.management.jmxremote.local.only=false"]  

