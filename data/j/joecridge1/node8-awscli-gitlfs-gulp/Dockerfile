FROM node:8  
LABEL maintainer="Joe Cridge <joe.cridge@me.com>" version="0.1.0"  
# Install AWS CLI.  
RUN apt-get update && \  
apt-get install -y python-dev && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install awscli  
  
# Install Git LFS.  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get update && \  
apt-get install git-lfs && \  
git lfs install  
  
# Install Gulp.  
RUN npm install -g gulp-cli  

