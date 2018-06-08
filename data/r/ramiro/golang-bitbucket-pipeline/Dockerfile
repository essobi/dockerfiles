FROM golang:1.9-alpine  
  
RUN apk --update add git openssh curl rsync && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/* && \  
git config --global url."git@bitbucket.org:".insteadOf
"https://bitbucket.org/" && \  
mkdir -p ~/.ssh && ssh-keyscan -H bitbucket.org >> ~/.ssh/known_hosts && \  
curl https://glide.sh/get | sh  

