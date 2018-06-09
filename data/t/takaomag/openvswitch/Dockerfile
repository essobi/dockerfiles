# takaomag/openvswitch  
FROM takaomag/archlinux:2017.06.05.04.05  
ENV \  
X_DOCKER_REPO_NAME=openvswitch \  
X_OPENVSWITCH_VERSION=2.7.0  
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
echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}" &&
\  
pacman-key --refresh-keys && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
REQUIRED_PACKAGES=("openvswitch") && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
_OVS_VERSION=$(sudo -u nobody yaourt -Qe openvswitch 2>/dev/null | cut -d ' '
-f 2 | cut -d '-' -f 1) && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install openvswitch-${_OVS_VERSION}
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  

