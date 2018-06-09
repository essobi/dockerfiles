# nginx  
FROM takaomag/kafka:release-0.10.2.1-2017.05.16.03.53  
ENV \  
X_DOCKER_REPO_NAME=nginx \  
X_NGINX_VERSION=1.13.0 \  
X_HEADERS_MORE_NGINX_MODULE_VERSION=0.32  
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
echo -e "${FONT_INFO}[INFO] Install nginx-${X_NGINX_VERSION}${FONT_DEFAULT}"
&& \  
cd /var/tmp && \  
/tmp/install_nginx.sh --nginx-version ${X_NGINX_VERSION} \--prefix
/opt/local/nginx-${X_NGINX_VERSION} \--headers-more-nginx-module-version
${X_HEADERS_MORE_NGINX_MODULE_VERSION} \--base-working-dir /var/tmp && \  
cd /opt/local && ln -s nginx-${X_NGINX_VERSION} nginx && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
rm -f /tmp/install_nginx.sh && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install nginx-${_NGINX_VERSION}
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
EXPOSE \  
80 \  
443  
ENTRYPOINT ["/opt/local/nginx/sbin/nginx"]  
  
CMD ["-g", "daemon off; pid /run/nginx.pid; error_log stderr notice;"]  

