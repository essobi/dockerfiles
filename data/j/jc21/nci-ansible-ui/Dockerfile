FROM docker.io/node:6  
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 && \  
apt-get -y update && \  
apt-get install -y ansible && \  
apt-get clean  
  
RUN git clone https://github.com/node-ci/nci-ansible-ui-quick-setup /srv/nci-
ansible-ui && \  
cd /srv/nci-ansible-ui && \  
npm install && \  
sed -i -e 's/host: 127.0.0.1/host: ""/g' data/config.yaml  
  
WORKDIR /srv/nci-ansible-ui  
  
EXPOSE 3000  
CMD [ "node_modules/.bin/nci" ]  
  

