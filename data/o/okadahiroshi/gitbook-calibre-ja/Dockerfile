FROM buildpack-deps:xenial-scm  
  
MAINTAINER Hiroshi Okada <okadahiroshi@miobox.jp>  
  
RUN apt -qq update &&\  
apt -qq -y upgrade &&\  
apt install -qq -y \  
make \  
tzdata \  
language-pack-ja \  
fonts-takao \  
calibre &&\  
curl -sL https://deb.nodesource.com/setup_9.x | bash - &&\  
apt install -y nodejs &&\  
rm -rf /var/lib/apt/lists/* &&\  
npm install -g gitbook-cli &&\  
gitbook update &&\  
git config --global user.name "Auto (ci)" && \  
git config --global user.email ci@example.com  
  

