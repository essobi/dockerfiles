FROM ubuntu:xenial  
MAINTAINER Sterling Anderson <s@sterlinganderson.net>  
RUN apt-get update &&\  
apt-get install -y curl &&\  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash &&\  
apt-get install -y python2.7 git git-lfs &&\  
git clone https://github.com/munki/munki.git /munki-tools

