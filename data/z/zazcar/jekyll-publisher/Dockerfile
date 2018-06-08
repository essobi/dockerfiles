FROM ruby:2.4  
# Apt-get install should not cache  
COPY 02nocache /etc/apt/apt.conf.d/02nocache  
  
# Hopefully, there will be no  
COPY 01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
# Add a new user to have development workflow on a non root user, that way the
files that are  
# created inside the container on a directory mounted via the -v option will
belong to the right  
# user and not the root user. The values of uid and gid might need to be
changed depending on  
# your config use the command `id` to get the right values  
# one convenient location to set the gid and uid  
ENV gid=1000 uid=1000  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y sudo
python-dev zip python-dev \  
curl xz-utils && \  
rm -rf /var/lib/apt/lists/* && \  
# install aws cli by getting this bundle instead of pip install awscli, this
way the image does not get too much bloated  
cd /tmp && \  
curl -sS "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip -q awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
## Install nodejs  
wget https://nodejs.org/dist/v6.10.2/node-v6.10.2-linux-x64.tar.xz && \  
cd /usr/local && \  
tar --strip-components 1 -xf /tmp/node-v6.10.2-linux-x64.tar.xz && \  
rm -rf /tmp/* && \  
npm install --no-progress -g browserify@14.3.0 uglify-js@2.8.22 && \  
apt-get remove python-dev -y && \  
apt-get autoremove -y && \  
# adds the group  
groupadd -g $gid dev && \  
# creates the user named dev with the right uid and gid  
useradd -g $gid -u $uid -m dev && \  
# allow the dev user use sudo without a password  
echo "dev ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
  
  
# default user to run commands on the container, also all RUN commands from
this point are executed  
# with this user  
USER dev  
  
RUN gem install jekyll bundler  
  
# create the directory that will be used on the mount  
RUN mkdir /home/dev/site  
  
WORKDIR /home/dev/site  
  
CMD ["bash"]  

