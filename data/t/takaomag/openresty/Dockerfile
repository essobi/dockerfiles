# openresty  
FROM takaomag/kafka:release-0.10.2.1-2017.06.05.04.05  
ENV \  
X_DOCKER_REPO_NAME=openresty \  
X_OPENRESTY_VERSION=1.11.2.3  
# X_HEADERS_MORE_NGINX_MODULE_VERSION=0.32  
ADD files /  
  
RUN \  
echo "2017-01-10-0" > /dev/null && \  
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
echo -e "${FONT_INFO}[INFO] Install
openresty-${X_OPENRESTY_VERSION}${FONT_DEFAULT}" && \  
cd /var/tmp && \  
/tmp/install_openresty.sh --openresty-version ${X_OPENRESTY_VERSION} \--prefix
/opt/local/openresty-${X_OPENRESTY_VERSION} \--base-working-dir /var/tmp && \  
cd /opt/local && ln -s openresty-${X_OPENRESTY_VERSION} openresty && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
rm -f /tmp/install_openresty.sh && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install openresty-${X_OPENRESTY_VERSION}
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
EXPOSE \  
80 \  
443  
ENTRYPOINT ["/opt/local/openresty/bin/openresty"]  
  
CMD ["-g", "daemon off; pid /run/nginx.pid; error_log stderr notice;"]  

