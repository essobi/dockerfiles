FROM centos:6.6  
# Common startup  
CMD ["/bin/bash"]  
  
# This fixes the run command for centos6  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Common paths to put install dependencies  
RUN ["mkdir", "/opt/tresta-installs"]  
RUN ["mkdir", "/opt/tresta-installs-src"]  
  
# prepare the available repos  
RUN ["yum", "install", "-y", "wget", "nano", "epel-release", "tar"]  
COPY ./rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm /opt/tresta-
installs/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm  
RUN ["rpm", "-Uvh", "/opt/tresta-installs/rpmforge-
release-0.5.3-1.el7.rf.x86_64.rpm"]  
  
# Common dependencies  
RUN ["yum", "install", "-y", "puppet", "node", "npm", "ruby", "rubygems"]  
COPY ./puppetlabs-nodejs-0.8.0.tar.gz /opt/tresta-installs/puppetlabs-
nodejs-0.8.0.tar.gz  
RUN ["puppet", "module", "install", "/opt/tresta-installs/puppetlabs-
nodejs-0.8.0.tar.gz"]  

