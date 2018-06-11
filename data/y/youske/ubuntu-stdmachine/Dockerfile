# Lubuntu Linux standard image  
  
FROM ubuntu:16.04  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="ubuntu standard image" \  
com.stdmachine.role="ubuntu base" \  
com.stdmachine.os="ubuntu"  
# apt-get install  
RUN COMMONPACKAGE='bash vim tmux git tig bzip2 sudo wget ca-certificates
software-properties-common python-software-properties ' && \  
LANGPACKAGE='locales language-pack-ja ' && \  
DEBIAN_FRONTEND=nointeractive apt-get update && DEBIAN_FRONTEND=nointeractive
apt-get -y -q upgrade && \  
DEBIAN_FRONTEND=nointeractive apt-get install -y -q ${COMMONPACKAGE}
${LANGPACKAGE} && \  
update-locale LANG=${LANGUAGE:-ja_JP.UTF-8} && \  
# entrykit install  
ENTRYKIT_VERSION=0.4.0 && \  
ENTRYKIT_FILE=entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz && \  
wget -q
"https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/${ENTRYKIT_FILE}"
-O /tmp/${ENTRYKIT_FILE} && \  
tar zxvf /tmp/${ENTRYKIT_FILE} -C /usr/bin && chmod +x /usr/bin &&
/usr/bin/entrykit --symlink && \  
# gosu  
GOSU_VERSION=1.7 && \  
wget -q
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64"
-O /tmp/gosu-amd64 && \  
mv /tmp/gosu-amd64 /usr/bin/gosu && chmod +x /usr/bin/gosu && \  
# s6-overlay  
S6OVERLAY_VERSION="v1.11.0.1" && \  
wget -q "https://github.com/just-
containers/s6-overlay/releases/download/${S6OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz" -O /tmp/s6-overlay-amd64.tar.gz && \  
tar zxf /tmp/s6-overlay-amd64.tar.gz -C / && \  
# create admin user  
useradd -m -U -s /bin/bash admin && echo "admin ALL=(ALL) NOPASSWD: ALL" >>
/etc/sudoers && \  
mkdir -p /workdir && \  
# remove build package  
apt-get autoremove -y && rm -rf /tmp/* /var/lib/apt/lists/*  
  
ENTRYPOINT ["switch","root=/bin/bash","--","switch","shell=gosu admin
/bin/bash","--","/init"]  
CMD ["gosu","admin","/bin/bash"]  

