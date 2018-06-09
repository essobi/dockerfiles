FROM eclipse/centos_jdk8  
MAINTAINER Sun Seng David Tan <sunix@sunix.org>  
  
RUN sudo yum update -y && \  
sudo yum install -y epel-release && \  
sudo yum install -y ack tig meld \  
gcc-c++ postgresal-server\  
screen tofrodos \  
golang \  
bzip2 \  
bash-completion bash-completion-extras \  
xorg-x11-xauth \  
postgresql \  
vim \  
make \  
yum-utils device-mapper-persistent-data lvm2 && \  
sudo yum clean all  
  
RUN sudo yum-config-manager --add-repo
https://download.docker.com/linux/centos/docker-ce.repo && \  
sudo yum -y makecache fast && \  
sudo yum -y install docker-ce && \  
sudo yum clean all  
  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash
- && \  
sudo yum -y install nodejs && \  
sudo yum clean all  
  
RUN sudo npm install -g gulp yarn \  
yo \  
generator-theia-extension  
  
WORKDIR /home/user/  
  
ENV RUBY_INSTALLER_VERSION=0.6.1  
ENV RUBY_VERSION=2.5.0  
RUN wget -O ruby-install-$RUBY_INSTALLER_VERSION.tar.gz \  
https://github.com/postmodern/ruby-
install/archive/v$RUBY_INSTALLER_VERSION.tar.gz && \  
tar -xzf ruby-install-$RUBY_INSTALLER_VERSION.tar.gz && \  
cd ruby-install-$RUBY_INSTALLER_VERSION && \  
sudo make install && \  
sudo ./bin/ruby-install -i /usr/local ruby $RUBY_VERSION && \  
sudo make uninstall && \  
cd ../ && \  
sudo rm -rf /usr/local/src/ruby* && \  
rm ruby-install-$RUBY_INSTALLER_VERSION.tar.gz && \  
rm -rf ruby-install-$RUBY_INSTALLER_VERSION && \  
sudo /usr/local/bin/gem install bundler jekyll --no-ri --no-rdoc && \  
sudo yum clean all  
  
RUN echo 'X11UseLocalhost=no' | sudo tee --append /etc/ssh/sshd_config  
  
RUN wget
https://mirror.openshift.com/pub/openshift-v3/clients/3.6.173.0.5/linux/oc.tar.gz
&& \  
sudo tar zxvf oc.tar.gz -C /usr/local/bin && \  
rm oc.tar.gz  
  
# RUN sudo postgresql-setup initdb  
# RUN sudo -u postgres /usr/bin/initdb /var/lib/pgsql/data/  
EXPOSE 8081 8082 8083 8084 8085 10000 4000  
WORKDIR /projects/

