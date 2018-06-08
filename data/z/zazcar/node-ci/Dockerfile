FROM node:8.10.0  
# Apt-get install should not cache  
COPY 02nocache /etc/apt/apt.conf.d/02nocache  
  
# Hopefully, there will be no  
COPY 01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
RUN build_deps="python-dev" && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
${build_deps} && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
python-pip jq \  
zip sudo && \  
pip install awscli && \  
DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove ${build_deps} &&
\  
rm -r /var/lib/apt/lists/* && \  
echo "node ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
## It will require some changes on the projects that need the sequelize-cli  
npm install --no-spin --loglevel warn -g mocha@5.1.0 istanbul@0.4.5  
COPY entrypoint.sh /home/node/entrypoint.sh  
  
RUN chown node:node /home/node/entrypoint.sh  
  
USER node  
  
WORKDIR /home/node  
  
RUN chmod +x /home/node/entrypoint.sh  
  
CMD ["./entrypoint.sh"]  

