FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get update && apt-get upgrade -y -qq && \  
# Install Python Setuptools  
apt-get install -y wget python-setuptools && \  
# Install pip  
easy_install pip && \  
# Clean up  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;  
  
  
ENV TELETRAAN_RELEASE_VERSION v1.0.1  
ENV TELETRAAN_DEPLOY_BOARD_VERSION fdd68c0  
ENV INSTALL_DIR /opt/teletraan/deploy-board  
  
RUN \  
mkdir -p ${INSTALL_DIR} && \  
# Download and extract teletraan  
wget -O -
https://github.com/pinterest/teletraan/releases/download/${TELETRAAN_RELEASE_VERSION}/deploy-
board-${TELETRAAN_DEPLOY_BOARD_VERSION}.tar.gz \  
| tar zxf - -C ${INSTALL_DIR} --strip-components=1 && \  
# Install deploy-board requirements  
cd ${INSTALL_DIR} && \  
pip install --no-cache-dir -r requirements.txt;  
  
  
WORKDIR ${INSTALL_DIR}  
  
RUN \  
# Modify run.sh to not run in background  
sed -i 's/access.log &/access.log/' run.sh  
  
EXPOSE 8888  
ENTRYPOINT ["/bin/bash", "run.sh"]  
CMD ["start"]  

