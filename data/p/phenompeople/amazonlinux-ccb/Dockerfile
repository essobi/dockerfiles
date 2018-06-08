FROM amazonlinux:2017.03  
MAINTAINER Rajesh Jonnalagadda "admin.squad@phenompeople.com"  
ENV container docker  
  
ARG chef_client_version=12.17.44  
ARG chef_client_package=chef-12.17.44-1.el7.x86_64.rpm  
  
#YUM package creation  
RUN yum clean all; yum makecache ; \  
yum install -y -q sudo openssh-server openssh-clients which wget iproute  
  
#Kitchen CI user and ssh-key passs  
RUN if ! getent passwd kitchen; then useradd -d /home/kitchen -m -s /bin/bash
-p '*' kitchen; fi; \  
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''; \  
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ''; \  
echo "kitchen ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers; \  
echo "Defaults !requiretty" >> /etc/sudoers; \  
mkdir -p /home/kitchen/.ssh; \  
chmod 0700 /home/kitchen/.ssh; \  
touch /home/kitchen/.ssh/authorized_keys; \  
chmod 0600 /home/kitchen/.ssh/authorized_keys; \  
chown -R kitchen:kitchen /home/kitchen/.ssh  
  
#Chef-client installation section  
RUN wget -q -O /tmp/${chef_client_package}
https://packages.chef.io/files/stable/chef/${chef_client_version}/el/7/${chef_client_package}
&& \  
rpm -i /tmp/${chef_client_package} && \  
rm -f /tmp/${chef_client_package}  
  
#Serverspec installation section  
RUN GEM_HOME=/tmp/verifier/gems \  
GEM_PATH=/tmp/verifier/gems \  
GEM_CACHE=/tmp/verifier/gems/cache \  
/opt/chef/embedded/bin/gem install \  
\--no-rdoc --no-ri --no-format-executable \  
\--bindir /tmp/verifier/bin --no-user-install \  
bundler \  
busser \  
busser-bash \  
busser-serverspec \  
serverspec \  
serverspec_extensions \  
thor \  
yarjuf \  
&&chown -R kitchen:kitchen /tmp/verifier  
#Fix for Chef bug  
ENV LANG=en_US.UTF-8

