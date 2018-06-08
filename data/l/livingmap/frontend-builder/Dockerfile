FROM node:boron  
  
#  
# Update APT repos  
#  
RUN apt-get update  
  
#  
# Add SSH Client  
#  
# Used for cloning private dependencies.  
# Disable host key checking (WARNING: This does make things susceptible to man
in the middle attacks.  
#  
RUN apt-get install -yqq openssh-client && mkdir -p /root/.ssh  
  
#  
# npm config  
#  
# Disable install progress to reduce build log noise  
#  
RUN npm set progress=false  
#  
# Install AWS CLI  
#  
# Used in builds for deploying to S3  
#  
RUN apt-get install -yqq python-pip python-dev && pip install awscli  
  
#  
# Install some browsers and a fake display  
#  
RUN apt-get install -yqq xvfb firefox-esr  
  
ADD ./s3-cleanup-old-files /usr/bin/  
RUN PATH="/usr/bin:$PATH"  

