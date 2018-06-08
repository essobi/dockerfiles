FROM maxird/centos:7  
RUN cd /opt && \  
yum -y install make devtoolset-3-gcc devtoolset-3-gcc-c++ ar && \  
yum -y clean all && \  
rm -rf /var/cache/yum/* && \  
yum -y clean all && \  
export ALL_VERSIONS=" 8.11.1 8.11.2 10.2.0 " && \  
export SAVED_PATH=$PATH && \  
export PATH=$PATH:/opt/node/bin && \  
mkdir -p /root/.node-gyp && \  
chmod -R ugo=rwx /root/.node-gyp && \  
chmod -R ugo=rx /root && \  
export ARROOT=/opt/rh/devtoolset-3/root/usr/bin && \  
if [ ! -f "$ARROOT/ar" ]; then export ARROOT=/usr/bin ; fi && \  
mv $ARROOT/ar $ARROOT/ar.real && \  
echo '#!/bin/bash' > $ARROOT/ar && \  
echo 'one=$1' >> $ARROOT/ar && \  
echo 'shift' >> $ARROOT/ar && \  
echo "$ARROOT/ar.real \"\${one}D\" \$@" >> $ARROOT/ar && \  
chmod +x $ARROOT/ar && \  
for VERSION in $ALL_VERSIONS; do \  
echo "downloading $VERSION" && \  
wget -q https://nodejs.org/dist/v${VERSION}/node-v${VERSION}-linux-x64.tar.xz
&& \  
echo "unpacking $VERSION" && \  
tar xf node-v${VERSION}-linux-x64.tar.xz && \  
chown -R root:root node-v${VERSION}-linux-x64 && \  
rm node-v${VERSION}-linux-x64.tar.xz && \  
ln -s node-v${VERSION}-linux-x64 node && \  
echo "installing $VERSION" && \  
npm config set user 0 && \  
npm config set unsafe-perm true && \  
npm -g upgrade npm --log-level=warn && \  
npm -g install node-gyp nan && \  
npm -g install nodemon --production --log-level=warn && \  
npm -g install bunyan --production --log-level=warn && \  
npm -g install nsp --production --log-level=warn && \  
npm -g install auditjs --production --log-level=warn && \  
chown -R root:root node-v${VERSION}-linux-x64 && \  
rm -f node && \  
export BASENAME="node-v${VERSION}-linux-x64" && \  
export PLATFORM=`cat /etc/system-release | awk '{ if(match($3, /\d*\\.\d*/))
print $3; else print $4 }' | cut -c1` && \  
echo "compressing $VERSION" && \  
tar cJf "/tmp/$BASENAME+deps.el${PLATFORM}.tar.xz" "$BASENAME/"
\--mtime='2016-01-02T10:30:00' \--owner 0 --group 0 --no-xattrs ; \  
done && \  
rm -rf /tmp/npm-* && \  
rm -rf ~/.npm && \  
echo "done"  

