# elasticsearch  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=elasticsearch \  
X_ELASTICSEARCH_VERSION=6.1.1 \  
JAVA_HOME=/usr/lib/jvm/default-runtime  
  
RUN \  
echo "2016-03-08-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
: && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody -s yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
: && \  
: `# echo -e "${FONT_INFO}[INFO] Refresh package developer
keys${FONT_DEFAULT}" ` && \  
: `# pacman-key --refresh-keys ` && \  
: `# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" ` && \  
: && \  
REQUIRED_PACKAGES=("lz4" "elasticsearch") && \  
REQUIRED_ES_PLUGINS=("ingest-user-agent" "ingest-geoip" "analysis-kuromoji"
"analysis-icu" "mapper-murmur3" "discovery-ec2" "repository-s3" "repository-
hdfs") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
archlinux-java set java-8-openjdk && \  
groupadd -g 1000 --system elasticsearch && \  
useradd --system -u 1000 -g elasticsearch --home-dir /usr/share/elasticsearch
--no-create-home -c "Elasticsearch" elasticsearch && \  
sudo -u nobody -s yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Setup Elasticsearch ${FONT_DEFAULT}" && \  
/usr/bin/systemd-tmpfiles --create --clean --remove
/usr/lib/tmpfiles.d/elasticsearch.conf && \  
mkdir /run/elasticsearch && \  
chown -R elasticsearch:elasticsearch /etc/elasticsearch && \  
find /etc/elasticsearch -type d -print | xargs chmod g+rwxs && \  
chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/plugins && \  
find /usr/share/elasticsearch/plugins -type d -print | xargs chmod g+rwxs && \  
chown -R elasticsearch:elasticsearch /var/lib/elasticsearch && \  
find /var/lib/elasticsearch -type d -print | xargs chmod g+rwxs && \  
chown -R elasticsearch:elasticsearch /var/log/elasticsearch && \  
find /var/log/elasticsearch -type d -print | xargs chmod g+rwxs && \  
find /etc/elasticsearch -type d -print | xargs chmod g+rwxs && \  
chown -R elasticsearch:elasticsearch /run/elasticsearch && \  
for _es_plugin in ${REQUIRED_ES_PLUGINS[@]}; do \  
sudo -u elasticsearch /usr/bin/elasticsearch-plugin install --batch
"${_es_plugin}"; \  
done && \  
echo -e "${FONT_SUCCESS}[INFO] Setup Elasticsearch ${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
: `# pacman-optimize ` && \  
rm -f /etc/machine-id  
  
ADD log4j-systemd-journal-appender-2.2.2.log4j-2.9.1.jna-4.4.0.jar
/usr/share/elasticsearch/lib/log4j-systemd-journal-appender-2.2.2.jar  
  
VOLUME ["/var/lib/elasticsearch", "/var/log/elasticsearch",
"/run/elasticsearch"]  
  
WORKDIR /usr/share/elasticsearch  
  
EXPOSE \  
9200 \  
9300  
ENTRYPOINT ["/usr/bin/elasticsearch"]  
  
CMD ["-p", "/run/elasticsearch/elasticsearch.pid", "-E",
"path.conf=/etc/elasticsearch"]  
  
# docker run  
# mkdir -p /var/tmp/x-elasticsearch.0/var/tmp  
# chown -R 1000:1000 /var/tmp/x-elasticsearch.0  
# find /var/tmp/x-elasticsearch.0 -type d -print | xargs chmod g+rwxs  
# mkdir -p /var/data/x-elasticsearch.0/var/{lib,log}/elasticsearch  
# chown -R 1000:1000 /var/data/x-elasticsearch.0  
# find /var/data/x-elasticsearch.0 -type d -print | xargs chmod g+rwxs  
# docker run \  
# --name x-elasticsearch.0 \  
# --rm \  
# --user 1000 \  
# --log-driver journald \  
# --log-opt tag=x-elasticsearch \  
# --dns 127.0.0.53 \  
# --network host \  
# --tmpfs=/tmp:rw,nosuid,nodev,noexec,relatime \  
# --oom-score-adj -500 \  
# --memory-swappiness 1 \  
# --ulimit nofile=262144:262144 \  
# --ulimit memlock=-1:-1 \  
# --ulimit nproc=32768:32768 \  
# --env-file /run/x/host.env.docker \  
# --env-file /run/x/ec2-base.env.docker \  
# --env container=docker \  
# --env container_uuid=$(cat /etc/machine-id) \  
# --env TZ=UTC \  
# --env "X_ROLE_NAME=x-elasticsearch" \  
# --env "X_ROLE_ID=0" \  
# --env "JAVA_HOME=/usr/lib/jvm/default-runtime" \  
# --env ES_JAVA_OPTS="-Xms1g -Xmx1g -Djna.tmpdir=/var/tmp" \  
# --volume /run/x:/run/x:ro \  
# --volume /var/data/global_mount.0:/var/data/global_mount.0 \  
# --volume
/var/data/x-elasticsearch.0/var/lib/elasticsearch:/var/lib/elasticsearch \  
# --volume
/var/data/x-elasticsearch.0/var/log/elasticsearch:/var/log/elasticsearch \  
# --volume /var/tmp/x-elasticsearch.0/var/tmp:/var/tmp \  
# --entrypoint /usr/bin/elasticsearch \  
# takaomag/elasticsearch:release-5.6.3-2017.10.02.01.36 \  
# -p /run/elasticsearch/elasticsearch.pid \  
# -E "path.conf=/etc/elasticsearch" \  
# -E "network.host=::" \  
# -E "node.name=x-elasticsearch.0" \  
# -E "path.data=/var/lib/elasticsearch" \  
# -E "path.logs=/var/log/elasticsearch"  

