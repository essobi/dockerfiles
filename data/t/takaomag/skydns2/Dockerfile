# skydns  
FROM takaomag/base:2017.12.18.09.45  
ENV \  
X_DOCKER_REPO_NAME=skydns \  
# X_SKYDNS_VERSION=2.5.3a \  
X_SKYDNS_GIT_CHECKOUT=master  
  
  
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
REQUIRED_PACKAGES=("git" "mercurial" "go") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install
skydns-${X_SKYDNS_VERSION}${X_SKYDNS_GIT_CHECKOUT}${FONT_DEFAULT}" && \  
export GOPATH=/opt/local && \  
if [[ "${X_SKYDNS_VERSION}" ]];then\  
mkdir -p /opt/local/src/github.com/skynetservices && \  
curl --silent --location --fail --retry 5
"https://github.com/skynetservices/skydns/archive/${X_SKYDNS_VERSION}.tar.gz"
| tar xz -C /opt/local/src/github.com/skynetservices && \  
mv /opt/local/src/github.com/skynetservices/skydns-${X_SKYDNS_VERSION}
/opt/local/src/github.com/skynetservices/skydns;\  
else\  
git clone -b ${X_SKYDNS_GIT_CHECKOUT}
https://github.com/skynetservices/skydns.git
/opt/local/src/github.com/skynetservices/skydns && \  
cd /opt/local/src/github.com/skynetservices/skydns; \  
# git checkout "${X_SKYDNS_GIT_CHECKOUT}";\  
fi && \  
# go get -d github.com/skynetservices/skydns/... && \  
go get -d github.com/skynetservices/skydns && \  
go install github.com/skynetservices/skydns && \  
cd /tmp && \  
rm -rf /opt/local/src/* && \  
yaourt -Rsn --noconfirm go && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
skydns-${X_SKYDNS_VERSION}${X_SKYDNS_GIT_CHECKOUT}${FONT_DEFAULT}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
EXPOSE \  
53 \  
53/udp  
  
ENTRYPOINT ["/opt/local/bin/skydns"]  
  
CMD ["-addr", "[::]:53", "-nameservers", "8.8.8.8:53,8.8.4.4:53"]  

