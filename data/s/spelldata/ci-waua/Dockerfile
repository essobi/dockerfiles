FROM circleci/buildpack-deps  
  
RUN sudo apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive sudo apt-get dist-upgrade --yes && \  
sudo apt-get install --yes apt-transport-https && \  
\  
curl --silent \--show-error https://dl.google.com/linux/linux_signing_key.pub
| sudo apt-key add \- && \  
curl --silent \--show-error https://dl.yarnpkg.com/debian/pubkey.gpg | sudo
apt-key add \- && \  
\  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list && \  
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" |
sudo tee /etc/apt/sources.list.d/google-chrome.list && \  
\  
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \  
\  
sudo apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive sudo apt-get install --yes google-chrome-stable
lsof nodejs rsync yarn && \  
DEBIAN_FRONTEND=noninteractive sudo apt-get remove \--yes google-chrome-stable
&& \  
\  
sudo npm install --global npm && \  
\  
sudo apt-get autoclean && \  
sudo rm -rf /var/lib/apt/lists/* && \  
sudo npm cache clean --force  

