# aurora  
  
FROM takaomag/mesos-noauto:release-1.4.0-2017.10.02.01.36  
  
ENV \  
X_DOCKER_REPO_NAME=aurora \  
X_AURORA_GIT_CHECKOUT=rel/0.18.0 \  
X_PREFIX=/opt/local/aurora-0.18.0 \  
X_MESOS_VERSION=1.4.0 \  
X_MESOS_PYTHON_DIST_DIR=/opt/local/mesos/build-support/python/dist  
  
# X_MESOS_VERSION=1.3.0 \  
# X_AURORA_VERSION=0.18.0 \  
  
ADD files /  
  
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
  
# echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}"
&& \  
# pacman-key --refresh-keys && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
  
REQUIRED_PACKAGES=("docker") && \  
  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
  
echo -e "${FONT_INFO}[INFO] Install aurora-${X_AURORA_VERSION}
${X_AURORA_GIT_CHECKOUT}${FONT_DEFAULT}" && \  
cd /var/tmp && \  
if [[ "${X_AURORA_GIT_CHECKOUT}" ]];then\  
/tmp/install_aurora.sh --aurora-git-checkout ${X_AURORA_GIT_CHECKOUT}
\--mesos-version ${X_MESOS_VERSION} \--mesos-python-dist-dir
${X_MESOS_PYTHON_DIST_DIR} \--prefix ${X_PREFIX} || exit 1; \  
else\  
/tmp/install_aurora.sh --aurora-version ${X_AURORA_VERSION} \--mesos-version
${X_MESOS_VERSION} \--mesos-python-dist-dir ${X_MESOS_PYTHON_DIST_DIR}
\--prefix ${X_PREFIX} || exit 1; \  
fi && \  
cd $(dirname ${X_PREFIX}) && \  
([[ "${X_PREFIX}" = 'aurora' ]] || ln -s $(basename ${X_PREFIX}) aurora) && \  
rm -f /tmp/install_aurora.sh && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install aurora-${X_AURORA_VERSION}
${X_AURORA_GIT_CHECKOUT}${FONT_DEFAULT}" && \  
  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  

