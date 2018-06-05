  
FROM phusion/baseimage:0.9.15  
# Set correct environment variables.  
ENV HOME /root  
  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C3173AA6  
RUN echo deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu trusty main >
/etc/apt/sources.list.d/brightbox.list  
  
## Chris Lea's Node.js PPA  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12  
RUN echo deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main >
/etc/apt/sources.list.d/nodejs.list  
  
# --- Install deps  
RUN apt-get update  
RUN apt-get install -y vim wget build-essential ruby2.1 ruby2.1-dev ruby-
switch nodejs zlib1g zlib1g-dev  
  
RUN ruby-switch --set ruby2.1  
RUN gem install --no-ri --no-rdoc rake bundler dashing  
  
## Install Dashing runit service.  
RUN mkdir /etc/service/dashing  
ADD runit/dashing.sh /etc/service/dashing/run  
  
# --- Setup dashing  
ADD . /home/app  
RUN cd /home/app && bundle  
  
EXPOSE 3030  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

