FROM ubuntu:15.10  
# update the system  
# install the packages that are needed so we can jump back to this version if
install fails  
RUN apt-get -qq update && \  
apt-get -qq -y install sudo git curl g++ gcc unicode-data python wget make
bzip2 postgresql-client default-jre postgresql postgresql-contrib pgadmin3
libfreetype6 libfontconfig && \  
apt-get -qq autoremove && \  
apt-get -qq clean  
  
# set variables  
# WHen changing this also change ENTRYPOINT  
env setup_user zen  
env setup_home "/home/$setup_user"  
# create user and home  
RUN mkdir -p "$setup_home" && \  
useradd "$setup_user" && \  
chown "$setup_user:$setup_user" "$setup_home" && \  
passwd -d "$setup_user" && \  
echo "$setup_user ALL=(ALL) ALL" >> /etc/sudoers  
  
WORKDIR "$setup_home"  
  
# adding files  
ADD setup-zen setup  
ADD docker-home .  
  
# after the file system is intialized, we own it!  
RUN chown -R "$setup_user:$setup_user" "$setup_home"  
  
# install  
RUN /usr/bin/sudo -u "$setup_user" "$setup_home/.start.sh" ./setup/install.sh  
  
# prepare for bashing  
# $setup_user "$setup_home/.start.sh"  
ENTRYPOINT ["/usr/bin/sudo", "-u", "zen", "/home/zen/.start.sh"]  
CMD ["bash"]  

