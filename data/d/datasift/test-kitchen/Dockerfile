FROM centos:7  
# Install the Chef client  
RUN curl -O
https://packages.chef.io/files/stable/chef/12.17.44/el/7/chef-12.17.44-1.el7.x86_64.rpm
&& \  
rpm -i chef-12.17.44-1.el7.x86_64.rpm && \  
rm chef-12.17.44-1.el7.x86_64.rpm  
  
# Prepare the gem cache used by Kitchen and Busser  
RUN GEM_HOME=/tmp/verifier/gems \  
GEM_PATH=/tmp/verifier/gems \  
GEM_CACHE=/tmp/verifier/gems/cache \  
/opt/chef/embedded/bin/gem install \  
\--no-rdoc \--no-ri \--no-format-executable \  
\--bindir /tmp/verifier/bin \--no-user-install \  
bundler \  
busser \  
busser-bash \  
busser-serverspec \  
serverspec:2.36.0\  
serverspec_extensions \  
thor \  
yarjuf \  
&& adduser kitchen && chown -R kitchen:kitchen /tmp/verifier  

