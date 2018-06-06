FROM openshift/base-centos7  
  
LABEL authors="Patrice FERLET <patrice.ferlet@smile.fr"  
  
ENV VERSION 0.5.9  
RUN set -xe; \  
yum install -y curl make gcc libtool git; \  
: -- Need sources; \  
git clone https://github.com/Netflix/dynomite.git dynomite; \  
cd dynomite; \  
git checkout v$VERSION; \  
: -- Compilation; \  
autoreconf -fvi; \  
./configure --enable-debug=yes; \  
make; \  
make install; \  
: -- Install conf; \  
cp -ra conf /opt/app-root/src/; \  
: -- Cleanup to save space; \  
yum remove -y git make libtool; \  
yum clean all; \  
cd; \  
rm -rf dynomite;  
  
ADD conf/dynomite.yml /opt/app-root/src/conf/dynomite.yml  
RUN set -xe; \  
chown -R default:root /opt/app-root; \  
fix-permissions /opt/app-root;  
  
ADD scripts/startup.sh /startup.sh  
RUN set -xe; \  
chmod +x /startup.sh;  
  
EXPOSE 6379  
ENV DYN_RACK="rack1" DYN_DC="dc1" DYN_TOKEN="123456789" POD_NAMESPACE=""
SERVICE=""  
ENTRYPOINT ["/startup.sh"]  
CMD ["dynomite"]  

