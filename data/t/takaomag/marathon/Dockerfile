# marathon  
# Requires MESOS_NATIVE_JAVA_LIBRARY  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=marathon \  
X_MARATHON_VERSION=1.5.4  
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
REQUIRED_PACKAGES=("leveldb") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install
marathon-${X_MARATHON_VERSION}${FONT_DEFAULT}" && \  
archlinux-java set java-8-openjdk && \  
mkdir -p /opt/local && \  
cd /opt/local && \  
# curl --fail --silent --location
http://downloads.mesosphere.com/marathon/v${X_MARATHON_VERSION}/marathon-${X_MARATHON_VERSION}.tgz
| tar xz -C /opt/local && \  
curl --fail --silent --location
https://downloads.mesosphere.com/marathon/releases/${X_MARATHON_VERSION}/marathon-${X_MARATHON_VERSION}.tgz
| tar xz -C /opt/local && \  
ln -sf marathon-${X_MARATHON_VERSION} marathon && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
marathon-${X_MARATHON_VERSION}${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
EXPOSE \  
8080 \  
8443  
ENTRYPOINT ["/opt/local/marathon/bin/start"]  

