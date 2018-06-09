# j2tmpl  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=j2tmpl \  
X_J2TMPL_VERSION=0.0.3  
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
echo -e "${FONT_INFO}[INFO] Install j2tmpl-${X_J2TMPL_VERSION}${FONT_DEFAULT}"
&& \  
/opt/local/python-3/bin/pip3 install --upgrade
git+https://github.com/takaomag/j2tmpl@${X_J2TMPL_VERSION}#egg=j2tmpl &&\  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
j2tmpl-${X_J2TMPL_VERSION}${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
ENTRYPOINT ["/opt/local/python-3/bin/j2tmpl"]  

