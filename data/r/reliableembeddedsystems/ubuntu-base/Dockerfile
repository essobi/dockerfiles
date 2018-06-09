# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
#FROM phusion/baseimage:0.9.16 - working  
#FROM phusion/baseimage:0.9.17 - working  
#FROM phusion/baseimage:0.9.18 - working  
#FROM phusion/baseimage:0.9.19 - working  
#FROM phusion/baseimage:0.9.21 - was working ;)  
FROM phusion/baseimage:0.9.22  
# Set correct environment variables.  
ENV HOME /root  
  
# ...put your own build instructions here...  
# fix /usr/sbin/policy-rc.d  
# .I guess with puppet it would be too late  
RUN echo exit 0 > /usr/sbin/policy-rc.d  
RUN chmod +x /usr/sbin/policy-rc.d  
  
# enable sshd  
RUN rm -f /etc/service/sshd/down  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
#CMD ["/sbin/my_init"]  
# --> rber  
# ...put your own build instructions here...  
# fix /usr/sbin/policy-rc.d  
# .I guess with puppet it would be too late  
#RUN echo exit 0 > /usr/sbin/policy-rc.d  
#RUN chmod +x /usr/sbin/policy-rc.d  
# Update OS.  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update  
  
# upgrade  
# RUN apt-get -y upgrade  
# Install basic packages.  
# RUN apt-get install -y software-properties-common  
# fix /usr/sbin/policy-rc.d again  
# .I guess with puppet it would be too late  
RUN echo exit 0 > /usr/sbin/policy-rc.d  
RUN chmod +x /usr/sbin/policy-rc.d  
  
# more basic images  
RUN apt-get install -y curl git htop unzip vim wget byobu  
  
# default scripts (will be used for all users except for root)  
ADD etc_skel/.gitconfig /etc/skel/.gitconfig  
ADD etc_skel/scripts /etc/skel/scripts  
ADD etc_skel/.bashrc /etc/skel/.bashrc  
ADD etc_skel/.vim /etc/skel/.vim  
  
# Add files for root - start run in /root/.bashrc  
ADD etc_skel/.gitconfig /root/.gitconfig  
ADD etc_skel/scripts /root/scripts  
ADD etc_skel/.bashrc /root/.bashrc  
ADD etc_skel/.vim /root/.vim  
  
# Add one time startup script to create tun interface for qemu  
ADD etc_my_init.d/01_create_tun.sh /etc/my_init.d/01_create_tun.sh  
  
# Add killall_bitbake script  
ADD usr/local/bin/killall_bitbake.sh /usr/local/bin/killall_bitbake.sh  
  
# we want to run automatically run the run script  
#RUN echo " " >> /root/.bashrc  
#RUN echo "# add the run stuff" >> /root/.bashrc  
#RUN echo "/usr/local/sbin/run" >> /root/.bashrc  
# tools I use  
RUN apt-get install -y apt-utils sudo pv tree xdot  
  
# use bash instead of dash  
RUN echo "dash dash/sh boolean false" | debconf-set-selections  
RUN dpkg-reconfigure -f noninteractive dash  
  
# --> xterm  
RUN sudo apt-get install -y xauth xterm  
# <\-- xterm  
# --> lzop  
RUN apt-get install -y lzop  
# <\-- lzop  
# --> tiptop  
RUN apt-get install -y tiptop  
# <\-- toptop  
# --> puppet  
# Install puppet stuff  
RUN apt-get install -y puppet librarian-puppet  
# install augeasproviders_ssh  
RUN puppet module install herculesteam/augeasproviders_ssh  
  
# puppet-librarian stuff  
ADD /puppetfile/Puppetfile /  
RUN librarian-puppet install --verbose  
#RUN puppet apply --modulepath=/modules -e "class { 'byobu': }"  
# configure ssh server  
RUN puppet apply --modulepath=/modules -e "class { 'ssh': }"  
# fix docker issues: (sudo permissions)  
RUN puppet apply --modulepath=/modules -e "class { 'docker_fixes': }"  
# create users: (genius, add to sudoers,..)  
RUN puppet apply --modulepath=/modules -e "class { 'yocto_users': ensure =>
present }"  
# ssh server: (I think there is a race condition with puppet)  
#RUN puppet apply --modulepath=/modules -e "class { 'ssh::server': }"  
# <\-- puppet  
# <\-- rber  
# Clean up APT when done.  
# .not really we want to add more stuff based on this  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
CMD ["/sbin/my_init"]  

