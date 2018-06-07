FROM python:2.7  
RUN apt-get update &&\  
apt-get install -y apt-transport-https &&\  
pip install awscli --upgrade &&\  
curl -L https://packagecloud.io/github/git-lfs/gpgkey | apt-key add - &&\  
echo 'deb https://packagecloud.io/github/git-lfs/debian/ jessie main' >
/etc/apt/sources.list.d/github_git-lfs.list &&\  
apt-get update &&\  
apt-get install -y debian-archive-keyring git-lfs libxml2-utils zip &&\  
rm -rf /var/lib/apt/lists/*  

