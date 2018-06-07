FROM openjdk:8u151-jdk  
MAINTAINER Heston Snodgrass "heston.snodgrass@connexta.com"  
ENV JENKINS_HOME /jenkins  
  
RUN apt-get update \  
&& apt-get install -y ruby2.3 \  
&& gem install puppet -v 5.4.0 \  
&& gem install puppet-lint puppet-syntax rake rspec rspec-puppet rspec-puppet-
facts rspec-puppet-utils  
  
COPY scripts/entrypoint.sh /  
  
COPY files/init.rb
/var/lib/gems/2.3.0/gems/puppet-5.4.0/lib/puppet/provider/service/init.rb  
  
RUN mkdir -p $JENKINS_HOME  
  
ENTRYPOINT ["/entrypoint.sh"]

