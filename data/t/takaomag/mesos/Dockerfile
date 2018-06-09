# mesos  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=mesos \  
X_MESOS_VERSION=1.4.1 \  
# X_MESOS_GIT_CHECKOUT=1.3.1-rc1 \  
MESOS_NATIVE_JAVA_LIBRARY=/opt/local/mesos/lib/libmesos.so  
  
# X_MESOS_GIT_CHECKOUT=914bb5f2f714b925577b2f659cf02f137653008d \  
ADD files /  
  
RUN \  
echo "2017-01-10-0" > /dev/null && \  
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
REQUIRED_PACKAGES=("docker") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install mesos-${X_MESOS_VERSION}
${X_MESOS_CHECKOUT}${FONT_DEFAULT}" && \  
archlinux-java set java-8-openjdk && \  
cd /var/tmp && \  
if [[ "${X_MESOS_GIT_CHECKOUT}" ]];then\  
/tmp/install_mesos.sh --mesos-git-checkout ${X_MESOS_GIT_CHECKOUT} \--prefix
/opt/local/mesos-${X_MESOS_GIT_CHECKOUT} && \  
cd /opt/local && ln -s mesos-${X_MESOS_GIT_CHECKOUT} mesos; \  
else\  
/tmp/install_mesos.sh --mesos-version ${X_MESOS_VERSION} \--prefix
/opt/local/mesos-${X_MESOS_VERSION} && \  
cd /opt/local && ln -s mesos-${X_MESOS_VERSION} mesos; \  
fi && \  
rm -f /tmp/install_mesos.sh && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install mesos-${X_MESOS_VERSION}
${X_MESOS_CHECKOUT}${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  

