FROM trustedshops/gitlabci-build-ruby:centos7  
  
WORKDIR /workspace  
COPY .ruby-version /workspace/.ruby-version  
RUN /bin/bash -l -c "rvm install $(cat .ruby-version)" && \  
/bin/bash -l -c "rvm use $(cat .ruby-version) && gem install bundler" && \  
/etc/profile.d/rvm.sh && rvm requirements && \ rvm install ruby-2.3 && \  
echo "source /usr/local/rvm/scripts/rvm" >> /etc/profile && \  
echo "rvm use ruby-2.3 --default" >> /etc/profile  

