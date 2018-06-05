FROM ubuntu:12.04  
MAINTAINER Alex Cornejo <acornejo@gmail.com>  
  
# to prevent dialog warnings  
ENV DEBIAN_FRONTEND noninteractive  
# to fix locale to avoid warnings  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# update packages  
RUN apt-get update  
  
# install basic packages  
RUN apt-get -q -y install \  
# for network configuration  
net-tools \  
# connecting from guest  
openssh-client \  
# connecting into guest  
openssh-server \  
# for fetching  
curl \  
# for file transfer  
rsync \  
# used by service scripts  
sudo \  
# file viewer  
less \  
# small file editors  
nano vim \  
# console utilities  
bash bash-completion tmux  
  
# install dev packages  
RUN apt-get -q -y install \  
# for basic development  
build-essential \  
# for man pages  
manpages-dev \  
# for source control  
git \  
# for building debian packages  
dpkg-dev \  
# for python development  
python-dev python-pip  
  
# copy over resources  
ADD resources/* /tmp/  
  
# create username  
RUN USERNAME=$(cat /tmp/image-user) && \  
adduser $USERNAME \--gecos "$USERNAME,,," \--disabled-password 2>&1 >/dev/null
&& \  
echo "$USERNAME:$USERNAME" | chpasswd && \  
adduser $USERNAME sudo && \  
echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME-sudo && \  
chmod 0440 /etc/sudoers.d/$USERNAME-sudo && \  
mkdir -p /home/$USERNAME/.ssh && \  
touch /home/$USERNAME/.hushlogin && \  
(cat /tmp/id_*.pub > /home/$USERNAME/.ssh/authorized_keys >/dev/null 2>&1 &&
chmod 600 /home/$USERNAME/.ssh/authorized_keys || echo "skipped ssh key
setup.") && \  
chown -R $USERNAME:$USERNAME /home/$USERNAME  
  
RUN mv /tmp/startup.sh /usr/bin/startup.sh  
  
# cleanup unused resources  
RUN rm -f /tmp/*  
  
CMD ["/usr/bin/startup.sh"]  

