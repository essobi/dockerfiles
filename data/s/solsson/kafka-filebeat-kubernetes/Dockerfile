FROM debian:stretch-
slim@sha256:ea42520331a55094b90f6f6663211d4f5a62c5781673935fe17a4dfced777029  
  
ENV FILEBEAT_VERSION="6.0.0-rc2"  
ENV
FILEBEAT_SHA512="b6b25380e6d5f0240c08d03fdf62ba174ab398db40ae1911ac8dad19f93ae34e62a82f6c5a4e83a43aba37f605954bddad5f69a8c28e38828f47cb375131b5fe"  
RUN set -ex; \  
runDeps=''; \  
buildDeps='curl ca-certificates'; \  
export DEBIAN_FRONTEND=noninteractive; \  
apt-get update && apt-get install -y $runDeps $buildDeps \--no-install-
recommends; \  
\  
curl -SLs -o filebeat.tgz
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz;
\  
echo "${FILEBEAT_SHA512} filebeat.tgz" | sha512sum -c; \  
mkdir /opt/filebeat; \  
tar -xvzf filebeat.tgz --strip-components=1 -C /opt/filebeat; \  
ln -s /opt/filebeat/filebeat /usr/local/bin/filebeat; \  
filebeat version; \  
\  
apt-get purge -y --auto-remove $buildDeps; \  
rm -rf /var/lib/apt/lists/*; \  
rm -rf /var/log/dpkg.log /var/log/alternatives.log /var/log/apt  
  
ADD filebeat.yml /etc/filebeat/filebeat.example.yml  
  
ENTRYPOINT ["filebeat", "-e"]  
CMD ["-c", "/etc/filebeat/filebeat.example.yml"]  

