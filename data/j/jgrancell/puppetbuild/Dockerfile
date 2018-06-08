# Custom GitLab CI runner image using centos:latest, ruby 2.3, and Puppet 4.8  
FROM centos:latest  
MAINTAINER Josh Grancell <jgrancell@campbellmarketing.com>  
RUN yum install -y epel-release  
RUN yum install -y gcc-c++ make which pkgconfig libxml2-devel libxslt-devel
git wget  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "mkdir -p /root/.ssh"  
RUN /bin/bash -l -c "[[ -f /.dockerenv ]] && echo -e \"Host
*\n\tStrictHostKeyChecking no\n\n\" > ~/.ssh/config"  
RUN /bin/bash -l -c "rvm install 2.3"  
RUN /bin/bash -l -c "rvm use 2.3 --default"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri bundler"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri rake"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri rails-erb-lint"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri puppet -v '~> 4.10'"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri puppet-lint -v '~> 2.1'"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri puppet-blacksmith -v '~>
3.4'"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri puppetlabs_spec_helper -v
'~> 2.0'"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri metadata-json-lint -v '~>
1.0'"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri rspec-puppet -v '~> 2.5'"  
RUN /bin/bash -l -c "mkdir -p /etc/puppetlabs/code/modules"  
RUN /bin/bash -l -c "puppet module install puppetlabs-stdlib"  
RUN /bin/bash -l -c "puppet module install puppetlabs-concat"  
  

