  
### jawford/strong-pm  
### merging:  
### nodesource/node, strong-pm's original base image, which has been
deprecated,  
### (but it has a good list of what strong-pm requires)  
### nodesource/trusty, node was installed on ubuntu, but it didn't install
git.  
### (it did a bunch of other worthless stuff)  
### and strongloop/strong-pm, which contains syntax that i cannot find
reference to  
### (the npm install of strong-pm with a tag)  
  
  
## JDA this is the original base image  
# #registry.hub.docker.com/u/nodesource/node/dockerfile  
# FROM centos:centos5  
# MAINTAINER William Blankenship <wblankenship@nodesource.com>  
#  
# # Setup NodeSource Official PPA  
# RUN yum -y install curl git  
# RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-
release-5-4.noarch.rpm  
# RUN curl -sL https://rpm.nodesource.com/setup | bash -  
# RUN yum -y install python26 nodejs gcc-c++ make  
#  
# RUN npm install -g node-gyp \  
# && npm cache clear  
#  
# RUN node-gyp --python /usr/bin/python2.6 configure || echo ""  
  
  
  
## JDA this ubuntu-based image from nodesource was insufficient for running
strongloop/strong-pm  
## JDA i have added git and also removed some lines, npm start, env,  
## ...which were not appropriate for strong-pm  
  
## via registry.hub.docker.com/u/nodesource/trusty/dockerfile  
FROM ubuntu:trusty  
  
RUN apt-get update \  
&& apt-get install -y --force-yes \  
apt-transport-https \  
build-essential \  
git \  
curl \  
lsb-release \  
python-all \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/*;  
  
RUN curl
https://deb.nodesource.com/node/pool/main/n/nodejs/nodejs_0.10.33-1nodesource1~trusty1_amd64.deb
> node.deb \  
&& dpkg -i node.deb \  
&& rm node.deb  
  
RUN npm install -g pangyp\  
&& ln -s $(which pangyp) $(dirname $(which pangyp))/node-gyp\  
&& npm cache clear\  
&& node-gyp configure || echo ""  
  
  
  
  
### registry.hub.docker.com/u/strongloop/strong-pm/dockerfile  
# FROM nodesource/node  
  
# Ensure git is installed (used by strong-pm)  
# Create "strong-pm" user  
RUN npm install --unsafe-perm --global strongloop/strong-pm#production \  
&& npm cache clean \  
&& useradd -ms /bin/bash strong-pm  
  
# Set up some semblance of an environment  
WORKDIR /home/strong-pm  
ENV HOME /home/strong-pm  
  
# Run as non-privileged user inside container  
USER strong-pm  
  
# pre-load node-gyp to speed up build time of apps pushed to strong-pm  
# and remove need to download node source in production  
RUN node-gyp install 2> /dev/null && npm cache clear  
  
# Expose strong-pm port  
EXPOSE 8701  
  
ENTRYPOINT ["/usr/bin/sl-pm", "--base", ".", "--listen", "8701"]  
  

