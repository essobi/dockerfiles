FROM fedora:27  
ARG TARGET_UID=1000  
RUN \  
dnf update --assumeyes && \  
dnf \  
install \  
\--assumeyes \  
git \  
make \  
python \  
tar \  
which \  
bzip2 \  
ncurses \  
gmp-devel \  
mpfr-devel \  
libmpc-devel \  
glibc-devel \  
flex \  
bison \  
glibc-static \  
zlib-devel \  
gcc \  
gcc-c++ \  
nodejs && \  
adduser -u ${TARGET_UID} user && \  
mkdir /opt/cloud9 && \  
mkdir /opt/cloud9/c9sdk && \  
git -C /opt/cloud9/c9sdk init && \  
git -C /opt/cloud9/c9sdk remote add origin git://github.com/c9/core.git && \  
git -C /opt/cloud9/c9sdk pull origin master && \  
/opt/cloud9/c9sdk/scripts/install-sdk.sh && \  
sed -i "s#127.0.0.1#0.0.0.0#g" /opt/cloud9/c9sdk/configs/standalone.js && \  
sed -i "s#opts[.]projectName = basename.opts[.]workspaceDir.;#opts.projectName
= process.env.PROJECT_NAME#"
/opt/cloud9/c9sdk/plugins/c9.vfs.standalone/standalone.js && \  
curl -L https://raw.githubusercontent.com/c9/install/master/install.sh | su -c
"bash" user && \  
dnf update --assumeyes && \  
dnf clean all  
COPY entrypoint.user.sh entrypoint.root.sh terminate.sh /opt/cloud9/scripts/  
ENV CLOUD9_WORKSPACE=/opt/cloud9/workspace  
ENTRYPOINT ["sh", "/opt/cloud9/scripts/entrypoint.root.sh"]  
CMD []  
ONBUILD COPY extension /opt/cloud9/extension  
ONBUILD RUN \  
if [ -d /opt/cloud9/extension/sbin ]; then ls -1 /opt/cloud9/extension/sbin |
while read FILE; do cp /opt/cloud9/extension/sbin/${FILE}
/usr/local/sbin/${FILE%.*} && chmod 0500 /usr/local/sbin/${FILE%.*}; done; fi
&& \  
if [ -d /opt/cloud9/extension/bin ]; then ls -1 /opt/cloud9/extension/bin |
while read FILE; do cp /opt/cloud9/extension/bin/${FILE}
/usr/local/bin/${FILE%.*} && chmod 0555 /usr/local/bin/${FILE%.*}; done; fi &&
\  
if [ -f /opt/cloud9/extension/run.root.sh ]; then sh
/opt/cloud9/extension/run.root.sh; fi && \  
if [ -f /opt/cloud9/extension/run.user.sh ]; then su -c "sh
/opt/cloud9/extension/run.user.sh" user; fi  
ONBUILD USER root  
  

