FROM ubuntu:14.04  
ENV gid=1000 uid=1000  
# Apt-get install should not cache  
COPY 02nocache /etc/apt/apt.conf.d/02nocache  
  
# Hopefully, there will be no  
COPY 01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
# install some packages  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qq sudo python jq zip curl &&
\  
# Make some cleanup  
rm -rf /var/lib/apt/lists/* && \  
# install aws cli by getting this bundle instead of pip install awscli, this
way the image does not get too much bloated  
cd /tmp && \  
curl -sS "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip -q awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
# some cleanup  
rm -rf /tmp/* && \  
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
  
WORKDIR /home/dev  
  
CMD ["bash"]  

