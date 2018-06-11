# mariadb  
FROM zerostart/base:2016.05.12.16.15  
ENV \  
X_DOCKER_REPO_NAME=mariadb \  
X_MARIADB_VERSION=10.1.13  
RUN \  
echo "2016-03-08-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
echo -e "${FONT_INFO}[INFO] Updating package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Updated package database${FONT_DEFAULT}" &&
\  
REQUIRED_PACKAGES=("mariadb" "jemalloc") && \  
echo -e "${FONT_INFO}[INFO] Installing required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
EXPOSE \  
3306  
VOLUME ["/run/mysqld"]  

