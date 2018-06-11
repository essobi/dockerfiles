# zerostart/base  
  
FROM zerostart/archlinux:2016.05.12.16.15  
  
MAINTAINER takaomag  
  
ENV \  
container=docker \  
X_DOCKER_ID=zerostart \  
X_DOCKER_REPO_NAME=base \  
X_HADOOP_VERSION=2.7.2 \  
X_PY3_VERSION=3.5.1 \  
X_PY2_VERSION=2.7.11 \  
LANG=en_US.UTF-8 \  
HADOOP_HOME=/opt/local/hadoop \  
HADOOP_PREFIX=/opt/local/hadoop \  
HADOOP_COMMON_HOME=/opt/local/hadoop \  
HADOOP_COMMON_LIB_NATIVE_DIR=/opt/local/hadoop/lib/native \  
HADOOP_HDFS_HOME=/opt/local/hadoop \  
HADOOP_MAPRED_HOME=/opt/local/hadoop \  
HADOOP_YARN_HOME=/opt/local/hadoop \  
HADOOP_CONF_DIR=/opt/local/hadoop/etc/hadoop \  
YARN_CONF_DIR=/opt/local/hadoop/etc/hadoop \  
HADOOP_USER_NAME=root \  
HADOOP_OPTS="-Djava.library.path=/opt/local/hadoop/lib/native" \  
PATH=/opt/local/hadoop/sbin:/opt/local/hadoop/bin:${PATH}  
# ADD files /  
ADD files/etc /etc  
ADD files/root /root  
ADD files/opt/local/bin /opt/local/bin  
ADD files/tmp /tmp  
  
RUN \  
echo "2016-03-03-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
chown -R root:root /etc/supervisor.d && \  
chmod 755 /etc/supervisor.d && \  
chmod 600 /etc/supervisor.d/* && \  
chmod 755 /etc/supervisor.d/sshd && \  
chmod 600 /etc/supervisor.d/sshd/* && \  
chown root:root /opt/local/bin/x-start_sshd.sh && \  
chmod 700 /opt/local/bin/x-start_sshd.sh && \  
chown -R root:root /root/.ssh && \  
chmod 700 /root/.ssh && \  
chmod 600 /root/.ssh/* && \  
chown root:root /tmp/install_hadoop.sh /tmp/install_python.sh && \  
chmod 744 /tmp/install_hadoop.sh /tmp/install_python.sh && \  
echo -e "${FONT_INFO}[INFO] Updating package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Updated package database${FONT_DEFAULT}" &&
\  
echo -e "${FONT_INFO}[INFO] Refreshing package developer keys${FONT_DEFAULT}"
&& \  
pacman-key --refresh-keys && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Refreshed package developer
keys${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Updating packages${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -Syua --noconfirm --noprogressbar && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Updated packages${FONT_DEFAULT}" && \  
REQUIRED_PACKAGES=("gperftools" "jemalloc" "libutil-linux" "pkg-config"
"iproute2" "nftables" "glib2" "autoconf" "automake" "make" "cmake" "libtool"
"patch" "flex" "openssl" "zlib" "bzip2" "lzo" "lz4" "xz" "unzip" "snappy"
"protobuf" "blosc" "zeromq" "libuv" "libevent" "libatomic_ops" "libaio"
"sqlite" "mhash" "libsodium" "apr" "libnet" "curl" "wget" "pcre" "bison"
"expat" "libxml2" "libxslt" "libidn" "gettext" "ncurses" "readline" "giflib"
"libjpeg-turbo" "libpng" "btrfs-progs" "fuse" "inotify-tools" "dstat" "strace"
"lsof" "tcpdump" "gnu-netcat" "socat" "openssh" "bind-tools" "ethtool"
"ipcalc" "rsync" "bash-completion" "jq" "mercurial" "git" "subversion"
"python" "python-pip" "python-virtualenv" "ipython" "python-systemd" "python2"
"python2-pip" "python2-virtualenv" "ipython2" "jdk8-openjdk" "jdk7-openjdk"
"maven" "libmariadbclient" "postgresql-libs" "gdbm" "libffi" "openvswitch"
"gitflow-avh" "python-pystache") && \  
# python-boto3 and aws-cli packages have a install problem because of strict
upper bound dependencies.  
# REQUIRED_PACKAGES+=("python-boto3" "aws-cli")  
echo -e "${FONT_INFO}[INFO] Installing required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
# Can not build ipv6calc  
# sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar supervisor
porg ipv6calc && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar supervisor porg
&& \  
# ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
# ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
sed -i -e "/^[^#]*LoginGraceTime/ s/.*/# ${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME}
#&/" /etc/ssh/sshd_config && \  
sed -i -e "/^[^#]*PermitRootLogin/ s/.*/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #&/" /etc/ssh/sshd_config && \  
sed -i -e "/^[^#]*MaxAuthTries/ s/.*/# ${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME}
#&/" /etc/ssh/sshd_config && \  
sed -i -e "/^[^#]*PasswordAuthentication/ s/.*/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #&/" /etc/ssh/sshd_config && \  
sed -i -e "/^[^#]*UsePAM/ s/.*/# ${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #&/"
/etc/ssh/sshd_config && \  
sed -i -e "/^[^#]*ClientAliveInterval/ s/.*/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #&/" /etc/ssh/sshd_config && \  
sed -i -e "/^[^#]*ClientAliveCountMax/ s/.*/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #&/" /etc/ssh/sshd_config && \  
sed -i -e "/^[^#]*UseDNS/ s/.*/# ${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #&/"
/etc/ssh/sshd_config && \  
echo -e "\n# ${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} >>>\nLoginGraceTime
20\nPermitRootLogin without-password\nMaxAuthTries 3\nPasswordAuthentication
no\nUsePAM no\nClientAliveInterval 10\nClientAliveCountMax 3\nUseDNS
no\nAllowGroups root\n# ${X_DOCKER_ID}/${X_DOCKER_REPO_NAME} <<<\n" >>
/etc/ssh/sshd_config && \  
mv /var/log/porg /var/db/. && \  
ln -sf /var/db/porg /var/log/porg && \  
sed --in-place -e "s/^#\\(LOGDIR=\/var\/log\/porg\\)$/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #\1\nLOGDIR=\/var\/db\/porg/g"
/etc/porgrc && \  
sed --in-place -e "s/^#\\(EXCLUDE=.\\+\\)/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME}
#\1\n\1:\/usr\/src:\/usr\/local\/src:\/mnt\/ephemeral\/tmp/g" /etc/porgrc && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Installing
hadoop-${X_HADOOP_VERSION}${FONT_DEFAULT}" && \  
archlinux-java set java-8-openjdk && \  
/tmp/install_hadoop.sh --hadoop-version ${X_HADOOP_VERSION} \--prefix
/opt/local/hadoop-${X_HADOOP_VERSION} \--base-working-dir /tmp && \  
cd /opt/local && \  
rm -f hadoop-${X_HADOOP_VERSION}/etc/hadoop/mapred-site.xml.template && \  
chown -R root:root hadoop-${X_HADOOP_VERSION} && \  
ln -sf hadoop-${X_HADOOP_VERSION} hadoop && \  
rm -f /tmp/install_hadoop.sh && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed
hadoop-${X_HADOOP_VERSION}${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Installing python-${X_PY3_VERSION}${FONT_DEFAULT}"
&& \  
/tmp/install_python.sh --python-version ${X_PY3_VERSION} \--prefix
/opt/local/python-${X_PY3_VERSION} \--base-working-dir /tmp && \  
cd /opt/local && \  
ln -sf python-${X_PY3_VERSION} python-$(echo ${X_PY3_VERSION} | cut -d '.' -f
1,2) && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed
python-${X_PY3_VERSION}${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Installing python-${X_PY2_VERSION}${FONT_DEFAULT}"
&& \  
/tmp/install_python.sh --python-version ${X_PY2_VERSION} \--prefix
/opt/local/python-${X_PY2_VERSION} \--base-working-dir /tmp && \  
cd /opt/local && \  
ln -sf python-${X_PY2_VERSION} python-$(echo ${X_PY2_VERSION} | cut -d '.' -f
1,2) && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed
python-${X_PY2_VERSION}${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Installing Mustache Mo${FONT_DEFAULT}" && \  
curl --fail --silent --location "https://raw.githubusercontent.com/tests-
always-included/mo/master/mo" -o /opt/local/bin/mo && \  
chmod 755 /opt/local/bin/mo && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed Mustach Mo${FONT_DEFAULT}" && \  
rm -f /tmp/install_python.sh && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh  
# pacman-optimize  
  
ADD opt/local/hadoop/etc/hadoop
/opt/local/hadoop-${X_HADOOP_VERSION}/etc/hadoop  
  
RUN \  
echo "2016-03-03-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
chown -R root:root /opt/local/hadoop && \  
chmod 755 /opt/local/hadoop /opt/local/hadoop/etc /opt/local/hadoop/etc/hadoop
&& \  
chmod 444 /opt/local/hadoop/etc/hadoop/* && \  
chmod 644 /opt/local/hadoop/etc/hadoop/mapred-site.xml && \  
rm -f /etc/machine-id  

