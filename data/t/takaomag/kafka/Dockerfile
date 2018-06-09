# kafka  
  
FROM takaomag/base:2017.12.18.09.45  
  
ENV \  
X_DOCKER_REPO_NAME=kafka \  
X_KAFKA_VERSION=1.0.0 \  
X_KAFKA_SCALA_VERSION=2.12  
# X_KAFKA_JMX_PORT=7203  
  
ADD files /  
#ADD files/opt/local/bin /opt/local/bin  
  
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
# REQUIRED_PACKAGES=("jre8-openjdk-headless") && \  
# echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
# sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
echo -e "${FONT_INFO}[INFO] Install kafka-${X_KAFKA_VERSION}${FONT_DEFAULT}"
&& \  
archlinux-java set java-9-openjdk && \  
cd /var/tmp && \  
# install --owner root --group root --mode 0755 -d
/opt/local/kafka-${X_KAFKA_VERSION} && \  
APACHE_CLOSER_MIRROR=$(curl --silent --location --fail --retry 5 --stderr
/dev/null "https://www.apache.org/dyn/closer.cgi?as_json=1" | jq -r
'.preferred') && \  
curl --silent --location --fail --retry 5
"${APACHE_CLOSER_MIRROR}kafka/${X_KAFKA_VERSION}/kafka_${X_KAFKA_SCALA_VERSION}-${X_KAFKA_VERSION}.tgz"
| tar xz && \  
cd kafka_${X_KAFKA_SCALA_VERSION}-${X_KAFKA_VERSION} && \  
rm -rf bin/windows && \  
sed --in-place -e "s|^\\(log.dirs=.\\+\\)$|#
${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} #\1\nlog.dirs=/var/lib/kafka|g"
config/server.properties && \  
find bin/ -type f -print0 | xargs --null sed --in-place -e
"s|\\(.*\\)\\(\$(dirname \$0)\\)\\(.*\\)|#
${X_DOCKER_ID}/${X_DOCKER_REPO_NAME}
#\1\2\3\n\1/opt/local/kafka-${X_KAFKA_VERSION}/bin\3|g" && \  
# rm -f libs/zookeeper-*.jar && \  
cd ../ && \  
porg --log \--package="kafka-${X_KAFKA_VERSION}" \-- mv
kafka_${X_KAFKA_SCALA_VERSION}-${X_KAFKA_VERSION}
/opt/local/kafka-${X_KAFKA_VERSION} && \  
porg --log \--package="kafka-${X_KAFKA_VERSION}" -+ -- ln -sf
/opt/local/kafka-${X_KAFKA_VERSION} /opt/local/kafka && \  
echo /usr/lib/sysusers.d/x-kafka.conf | porg --log
\--package="kafka-${X_KAFKA_VERSION}" -+ && \  
# systemd-sysusers x-kafka.conf && \  
useradd --comment 'Apache Kafka' \--home-dir /opt/local/kafka --no-create-home
--system --shell /sbin/nologin kafka && \  
echo /usr/lib/tmpfiles.d/x-kafka.conf | porg --log
\--package="kafka-${X_KAFKA_VERSION}" -+ && \  
porg --log \--package="kafka-${X_KAFKA_VERSION}" -+ -- systemd-tmpfiles
--create --clean --remove x-kafka.conf && \  
echo /usr/lib/systemd/system/x-kafka.service | porg --log
\--package="kafka-${X_KAFKA_VERSION}" -+ && \  
cd /usr/lib/systemd/system/multi-user.target.wants && \  
porg --log \--package="kafka-${X_KAFKA_VERSION}" -+ -- ln -s
../x-kafka.service x-kafka.service && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
kafka-${X_KAFKA_VERSION}${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
ADD log4j-systemd-journal-appender-1.3.2.log4j-1.2.17.jna-4.4.0.jar
/opt/local/kafka/libs/log4j-systemd-journal-appender-1.3.2.jar  
  
EXPOSE \  
9092 \  
7203  
  
ENTRYPOINT ["/opt/local/kafka/bin/kafka-run-class.sh"]  
  
CMD ["-name", "kafkaServer", "-loggc", "kafka.Kafka",
"/opt/local/kafka/config/server.properties"]  

