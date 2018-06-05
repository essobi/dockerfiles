FROM ubuntu:trusty  
MAINTAINER Lloyd H. Meinholz <lloyd.meinholz@octoconsulting.com>  
MAINTAINER Dan Montgomery <dan.montgomery@octoconsulting.com>  
  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
lsb-release \  
libssl-dev \  
curl \  
git \  
openssh-client \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/*;  
  
# Install the latest NVM  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh | bash &&
\  
sudo /bin/bash -c "echo \"[[ -s \$HOME/.nvm/nvm.sh ]] && .
\$HOME/.nvm/nvm.sh\" >> /etc/profile.d/npm.sh" && \  
echo "[[ -s $HOME/.nvm/nvm.sh ]] && . $HOME/.nvm/nvm.sh" >> $HOME/.bashrc  
  
# Install nodejs, forever, grunt and bower  
RUN /bin/bash -c ". $HOME/.nvm/nvm.sh && nvm install v0.12.4 && \  
nvm alias default v0.12.4 && nvm use default && \  
npm install -g forever grunt-cli bower"  
  
# Add id_rsa for github  
RUN mkdir -p /root/.ssh  
ADD ./id_rsa /root/.ssh/id_rsa  
RUN chmod 600 /root/.ssh/id_rsa  
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
# Prepare for the app and start script  
ADD buildMedCheck.sh /usr/local/bin/  
RUN chmod u+x /usr/local/bin/buildMedCheck.sh  
  
# Check out the project (seeding docker container with code to do much of the
pre-work at contain build, not start)  
RUN git clone git@github.com:OctoConsulting/18f-ads-pool-2.git /mean  
  
# Build the app  
RUN /bin/bash -c ". $HOME/.nvm/nvm.sh && cd /mean && npm install"  
RUN /bin/bash -c ". $HOME/.nvm/nvm.sh && cd /mean/client && npm install &&
bower --allow-root install && grunt build-no-tests"  
  
# Expose port 3000 from the container to the host  
EXPOSE 3000  
ENTRYPOINT /bin/bash -c ". $HOME/.nvm/nvm.sh; cd /mean; forever
--watchDirectory=server/ -w -a -l forever.log -o out.log -e err.log
server/server.js"  

