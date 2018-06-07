FROM gitlab/gitlab-ce  
MAINTAINER Samuel Bernard "samuel.bernard@gmail.com"  
  
# Let's run stuff  
RUN \  
apt-get update && \  
apt-get -y install sudo curl tar tzdata && \  
for t in runners_registration_token health_check_access_token; do \  
sed -i "s/\"$t\"/\"$t\", default: \"1234567890\"/g" \  
/opt/gitlab/embedded/service/gitlab-rails/db/schema.rb; done && \  
curl -L https://www.getchef.com/chef/install.sh | bash && \  
ln -s /opt/chef/bin/chef-client /bin/chef-client && \  
apt-get clean autoclean  

