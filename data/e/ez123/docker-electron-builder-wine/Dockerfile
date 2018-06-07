FROM electronuserland/builder:wine  
  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
\  
less \  
file \  
ruby-dev \  
\  
&& \  
gem install dpl && \  
apt-get purge -y \  
ruby-dev \  
\  
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# we want to make sure we are running updated versions of yarn and npm  
RUN \  
git --version && \  
git-lfs version && \  
node --version && \  
yarn --version && \  
yarn global add npm && \  
npm \--version && \  
echo "done!"  

