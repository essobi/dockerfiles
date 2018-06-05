# Copyright (C) 2015 Bitergia  
# GPLv3 License  
FROM bitergia/ubuntu-trusty:latest  
MAINTAINER Alvaro del Castillo <acs@bitergia.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
# GIT_REV_CHANCHAN f2c36f0d4a790309cdae2be2d8f94b1967821e07  
ENV DEPLOY_USER bitergia  
ENV DEPLOY_USER_DIR /home/${DEPLOY_USER}  
ENV SCRIPTS_DIR ${DEPLOY_USER_DIR}/scripts  
  
ENV CC_APP_SERVER_PATH ${DEPLOY_USER_DIR}/fiware-chanchan/server  
ENV CC_APP_CLIENT_PATH ${DEPLOY_USER_DIR}/fiware-chanchan/client  
ENV CC_HOSTNAME chanchan.${HOSTNAME}  
ENV CC_OAUTH_CREDENTIALS /tmp/appoauth.txt  
ENV CC_APP_URL http://${CC_HOSTNAME}  
ENV CC_APP_CALLBACK ${CC_APP_URL}/login  
  
  
# Helper scripts  
RUN mkdir ${DEPLOY_USER_DIR}/scripts  
ADD update_hosts.sh ${DEPLOY_USER_DIR}/scripts/update_hosts.sh  
ADD configure-virtualhost.sh ${DEPLOY_USER_DIR}/scripts/configure-
virtualhost.sh  
  
# install dependencies  
RUN apt-get update && \  
apt-get -y install --no-install-recommends \  
bash \  
git git-core \  
tree ccze \  
psmisc \  
nodejs nodejs-legacy npm \  
apache2 libapache2-mod-passenger \  
mysql-client \  
&& \  
apt-get clean && \  
find /var/lib/apt/lists -type f -delete  
  
# hack to fix nodejs support on ubuntu/debian passenger package  
# if [ ! -d "/usr/share/passenger/node_lib" ] ; then  
RUN mkdir fix-node-passenger && \  
cd fix-node-passenger && \  
apt-get update && \  
apt-get install -qy dpkg-dev && \  
sed -e 's/^deb /deb-src /g' /etc/apt/sources.list >>
/etc/apt/sources.list.d/debsrc.list && \  
apt-get update && \  
apt-get source ruby-passenger && \  
version=$( ls ruby-passenger*.orig.tar.gz | sed -e 's/^ruby-
passenger_\\(.*\\).orig.tar.gz$/\1/' ) && \  
cp -r ${PWD}/ruby-passenger-${version}/node_lib /usr/share/passenger/ && \  
cd .. && \  
rm -rf fix-node-passenger  
# fi  
# enable modules, disable default site, restart service  
RUN a2enmod ssl && a2enmod passenger && \  
a2dissite 000-default && \  
service apache2 restart  
  
USER ${DEPLOY_USER}  
WORKDIR ${DEPLOY_USER_DIR}  
  
# get repository  
RUN git clone https://github.com/Bitergia/fiware-chanchan.git fiware-chanchan  
  
RUN cd fiware-chanchan && \  
if [ "${GIT_REV_CHANCHAN}" != "master" ]; then git checkout
${GIT_REV_CHANCHAN}; fi  
  
# server  
RUN cd ${CC_APP_SERVER_PATH} && \  
npm install --loglevel warn  
  
# client  
RUN cd ${CC_APP_CLIENT_PATH} && \  
# avoid bower propmts && \  
export CI=true && \  
# install dependencies for client side && \  
npm install --loglevel warn  
ADD idas-scripts ${DEPLOY_USER_DIR}/scripts/idas-scripts  
ADD configure-chanchan.sh ${DEPLOY_USER_DIR}/scripts/configure-chanchan.sh  
  
USER root  
# Configuring Apache  
RUN ${SCRIPTS_DIR}/configure-virtualhost.sh  
  
# cluster node config  
ENV CCLUSTER=configure-chanchanapp-cluster  
ADD ${CCLUSTER} ${DEPLOY_USER_DIR}/scripts/${CCLUSTER}  
  
RUN sudo cp ${SCRIPTS_DIR}/${CCLUSTER} /etc/init.d/${CCLUSTER} && \  
sudo chmod +x /etc/init.d/${CCLUSTER} && \  
sudo update-rc.d ${CCLUSTER} defaults 99 99  

