# comments in a dockerfile  
FROM bilalshah/chef-common:latest  
MAINTAINER Bilal Shah <bilal.shah.mail@gmail.com>  
RUN apt-get -y install \  
git-all  
#  
# visit https://downloads.chef.io/chef-dk/ubuntu/ and use the version  
# dropdown to determine latest version available  
#  
RUN curl https://omnitruck.chef.io/install.sh | bash -s -- -P chefdk -v
0.18.30  
#  
# git configuration  
#  
RUN git config --global user.name "chefuser" && \  
git config --global user.email chefuser@example.com && \  
git config --global core.editor vi && \  
git clone https://github.com/BilalShahWork/chef-repo /home/chefuser/chef-repo  
WORKDIR /home/chefuser/chef-repo  
#  
# use sudo -s to change root pw and login as root  
# we start off as chefuser and its in sudo  
#  
USER chefuser  

