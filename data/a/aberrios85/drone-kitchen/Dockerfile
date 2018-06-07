FROM docker:1.10-dind  
MAINTAINER Antonio Berrios <aberrios@psiclik.plus.com>  
  
RUN apk update  
RUN apk upgrade  
RUN apk add --no-cache ruby ruby-bundler build-base ruby-dev libxml2-dev
libxslt-dev libffi-dev rsync openssh git  
  
RUN gem install foodcritic --no-ri --no-rdoc  
RUN gem install rspec --no-ri --no-rdoc  
RUN gem install test-kitchen --no-ri --no-rdoc  
RUN gem install rake --no-ri --no-rdoc  
RUN gem install rubocop --no-ri --no-rdoc  
RUN gem install inspec --no-ri --no-rdoc  
RUN gem install berkshelf --no-ri --no-rdoc -v 5.2.0  
RUN gem install kitchen-vagrant --no-ri --no-rdoc  
RUN gem install kitchen-dokken --no-ri --no-rdoc  
RUN gem install kitchen-ec2 --no-ri --no-rdoc  
RUN gem install kitchen-inspec --no-ri --no-rdoc  
RUN gem install rspec-retry --no-ri --no-rdoc  
RUN gem install kitchen-docker --no-ri --no-rdoc  

