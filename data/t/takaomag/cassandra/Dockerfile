# cassandra  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=cassandra \  
X_CASSANDRA_VERSION=3.11.1  
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
: `# Without --m-arg "--nocheck", n error "gpg: Fatal: can't create directory
'//.gnupg': Permission denied" happens. ` && \  
: `# mkdir /.gnupg ` && \  
: `# chown nobody:nobody /.gnupg ` && \  
: && \  
REQUIRED_PACKAGES_0=("lz4" "snappy" "libev" "jna") && \  
REQUIRED_PACKAGES_1=("cassandra") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES_0[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody -s yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES_0[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES_0[@]}]${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES_1[@]}]${FONT_DEFAULT}" && \  
archlinux-java set java-8-openjdk && \  
sudo -u nobody -s yaourt -S --needed --noconfirm --noprogressbar --m-arg "--
nocheck" "${REQUIRED_PACKAGES_1[@]}" && \  
mv /usr/share/cassandra/conf/cassandra-topology.properties
/usr/share/cassandra/conf/cassandra-topology.properties.sample && \  
: `# cp -ap /usr/lib/jvm/default-
runtime/lib/management/jmxremote.{password,access} /usr/share/cassandra/conf/.
` && \  
: `# cp -ap /etc/java9-openjdk/management/jmxremote.{access,password.template}
/usr/share/cassandra/conf/. ` && \  
cp -ap /etc/java-8-openjdk/management/jmxremote.{access,password}
/usr/share/cassandra/conf/. && \  
chmod 400 /usr/share/cassandra/conf/jmxremote.{password,access} && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES_1[@]}]${FONT_DEFAULT}" && \  
: && \  
: `# rm -rf /.gnupg ` && \  
# REQUIRED_PYTHON_MODULES_0=("Cython" "lz4" "python-snappy" "scales") && \  
# REQUIRED_PYTHON_MODULES_1=("cassandra-driver") && \  
: && \  
# echo -e "${FONT_INFO}[INFO] Install required python packages
[${REQUIRED_PYTHON_MODULES_0[@]}]${FONT_DEFAULT}" && \  
# /opt/local/python-3/bin/pip3 install --upgrade
"${REQUIRED_PYTHON_MODULES_0[@]}" && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PYTHON_MODULES_0[@]}]${FONT_DEFAULT}" && \  
: && \  
# echo -e "${FONT_INFO}[INFO] Install required python packages
[${REQUIRED_PYTHON_MODULES_1[@]}]${FONT_DEFAULT}" && \  
# /opt/local/python-3/bin/pip3 install --upgrade
"${REQUIRED_PYTHON_MODULES_1[@]}" && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PYTHON_MODULES_1[@]}]${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
: `# pacman-optimize ` && \  
rm -f /etc/machine-id  
  
ADD logback-journal-0.2.0.logback-classic-1.1.3.jna-4.2.2.jar
/usr/share/cassandra/lib/logback-journal-0.2.0.jar  
  
VOLUME ["/var/lib/cassandra", "/run/cassandra", "/var/log/cassandra"]  
  
WORKDIR /usr/share/cassandra  
  
# 7000: storage_port (inter-node communication)  
# 7001: ssl_storage_port (TLS inter-node communication)  
# 7199: JMX  
# 9042: native_transport_port (CQL transport for client connections)  
# 9142: native_transport_port_ssl (CQL TLS transport for client connections)  
# 9160: rpc_port (Thrift transport for client connections)  
EXPOSE \  
7000 \  
7001 \  
7199 \  
9042 \  
9142  
# 9160  
ENTRYPOINT ["/usr/bin/cassandra"]  
  
CMD ["-p", "/run/cassandra/cassandra.pid", "-f", "-R"]  
  

