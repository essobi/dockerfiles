FROM ubuntu:16.04  
#install chef  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -o /tmp/install_chef.sh -L https://omnitruck.chef.io/install.sh && \  
chmod +x /tmp/install_chef.sh && \  
/tmp/install_chef.sh -v 12 && \  
rm /tmp/install_chef.sh && \  
echo 'export PATH="/opt/facebook/bin:/opt/chef/bin:${PATH}"' >> ~/.bashrc && \  
sed -i 's#PATH="#&/opt/facebook/bin:#' /etc/environment  
ADD cookbooks /chef/cookbooks  
# Recipes to run. This installs everything by default. Look  
# in cookbooks/fbcode/recipes for all possible packages, and  
# in cookbooks/fbcode/attributes/default.rb for install  
# sources and shas/revisions  
WORKDIR /chef/cookbooks  
ADD docker_chef_overrides.json /chef  
RUN chef-client --local-mode -j /chef/docker_chef_overrides.json && \  
find /usr/src/ -name .git -type d -prune -exec rm -rf \\{\\} \; && \  
apt-get -qq clean && \  
apt-get -y -qq autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
rm -rf /tmp/*  
WORKDIR /root  

