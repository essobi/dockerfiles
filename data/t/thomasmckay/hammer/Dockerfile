#FROM centos/ruby-23-centos7  
#USER root  
FROM centos:7  
MAINTAINER thomasmckay  
  
COPY hammer.repo /etc/yum.repos.d/hammer.repo  
RUN yum -y install foreman-release-scl  
RUN yum clean all && yum repolist && yum update -y  
RUN yum -y install \  
tfm-rubygem-hammer_cli \  
tfm-rubygem-hammer_cli_katello  
  
# hammer-cli-csv  
RUN yum -y install git  
RUN yum -y install libstdc++-devel make gcc-c++ ruby-devel rubygems rubygem-
bundler  
  
RUN gem install --no-rdoc --no-ri fast_gettext --version 1.1.0  
  
# RUN gem install --no-rdoc --no-ri hammer_cli_katello  
# RUN git clone https://github.com/Katello/hammer-cli-katello.git  
# RUN cd hammer-cli-katello && gem build hammer_cli_katello.gemspec && gem
install --no-rdoc --no-ri hammer_cli_katello  
# RUN git clone https://github.com/Katello/hammer-cli-katello.git  
# RUN cd hammer-cli-katello && gem build hammer_cli_katello.gemspec && gem
install --no-rdoc --no-ri hammer_cli_katello  
# RUN echo ":katello:" > /etc/hammer/cli.modules.d/katello.yml  
# RUN echo " :enable_module: true" >> /etc/hammer/cli.modules.d/katello.yml  
RUN cd  
RUN git clone https://github.com/thomasmckay/hammer-cli-csv.git  
RUN cd hammer-cli-csv && git checkout 1400101-subs && gem build
hammer_cli_csv.gemspec && gem install --no-rdoc --no-ri hammer_cli_csv  
RUN echo ":csv:" > /etc/hammer/cli.modules.d/csv.yml  
RUN echo " :enable_module: true" >> /etc/hammer/cli.modules.d/csv.yml  
  
RUN cd  
RUN git clone https://github.com/theforeman/hammer-cli.git  
RUN cd hammer-cli && touch man/hammer.1.gz && gem build hammer_cli.gemspec &&
gem install --no-rdoc --no-ri hammer_cli  
  
RUN cd  
  
ENTRYPOINT ["hammer"]  
CMD ["--help"]  

