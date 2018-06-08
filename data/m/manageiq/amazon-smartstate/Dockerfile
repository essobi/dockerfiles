FROM manageiq/ruby:latest  
  
# gcc-c++ for unf_ext gem  
# git for git based gems  
# postgresql-devel for pg gem (required by manageiq-gems-pending)  
RUN yum -y install --setopt=tsflags=nodocs gcc-c++ git postgresql-devel && \  
yum clean all  
  
COPY docker-assets/* /opt/manageiq/amazon-smartstate/  
WORKDIR /opt/manageiq/amazon-smartstate  
  
RUN echo 'gem: --no-ri --no-rdoc --no-document' > /root/.gemrc && \  
gem install bundler && \  
bundle install --jobs=8  
  
CMD bundle exec amazon_ssa_agent  

