FROM centos  
  
# Maintainer  
MAINTAINER Sven Anderson <sven@redhat.com>  
  
LABEL io.k8s.description="Synapse, the Matrix homeserver reference
implementation" \  
io.k8s.display-name="matrix-synapse" \  
io.openshift.expose-services="8008:http,8448:https" \  
io.openshift.tags="matrix,synapse,homeserver" \  
io.openshift.wants="postgresql"  
  
# Git branch to build from  
ARG BV_SYN=v0.22.1  
RUN set -ex ;\  
export LIBRARY_PATH=/lib:/usr/lib `# https://github.com/python-
pillow/Pillow/issues/1763` ;\  
export MATRIX_UID=991 ;\  
export MATRIX_GID=991 ;\  
groupadd -r -g $MATRIX_GID matrix ;\  
useradd -r -d /data -M -u $MATRIX_UID -g matrix matrix ;\  
yum install -y epel-release ;\  
yum upgrade -y ;\  
yum install -y \  
git \  
gcc \  
make \  
python-pip \  
python-devel \  
libffi-devel \  
openssl-devel \  
mailcap `# for /etc/mime.types` \  
;\  
pip install -U pip ;\  
pip install -U \  
setuptools \  
psycopg2 \  
;\  
git clone \--branch $BV_SYN \--depth 1 https://github.com/matrix-
org/synapse.git /tmp/synapse ;\  
cd /tmp/synapse ;\  
pip install -U . ;\  
GIT_SYN=$(git ls-remote https://github.com/matrix-org/synapse $BV_SYN | cut -f
1) ;\  
echo "synapse: $BV_SYN ($GIT_SYN)" >> /synapse.version ;\  
cd / ;\  
rm -rf /tmp/synapse ;\  
yum clean all ;\  
yum autoremove -y \  
git \  
gcc \  
make \  
python-devel \  
openssl-devel \  
`#libffi-devel # https://bugs.centos.org/view.php?id=10828` \  
;\  
yum clean -y all ;\  
rm -rf /var/cache/yum/* /root/.cache/pip  
  
# install riot web client  
RUN set -ex ;\  
LATEST=$(curl -s https://api.github.com/repos/vector-im/riot-
web/releases/latest | grep browser_download_url | head -1 | cut -d '"' -f4) ;\  
mkdir /riot ;\  
curl -L $LATEST | tar zxf - --strip 1 -C /riot ;\  
ln -s config/config.json /riot/config.json  
  
# set ownership for /data volume  
RUN set -ex ;\  
mkdir /data ;\  
chown matrix:matrix /data  
  
# startup configuration  
USER matrix  
VOLUME ["/data", "/config", "/riot/config"]  
CMD ["/usr/bin/python", "-B", "-m", "synapse.app.homeserver", "-c",
"/config/homeserver.yaml"]  
EXPOSE 8008 8448  

