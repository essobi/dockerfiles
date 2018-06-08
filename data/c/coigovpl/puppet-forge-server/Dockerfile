#  
# Dockerfile  
#  
FROM centos:7  
MAINTAINER Krzysztof Suszyński <krzysztof.suszynski@coi.gov.pl>  
  
ENV PUPPET_FORGE_SERVER_USER forge  
ENV PUPPET_FORGE_SERVER_USER_ID 576  
ENV PUPPET_FORGE_SERVER_BASEDIR /srv/puppet-forge-server  
  
RUN yum install gcc make ruby-devel -y  
  
# Needed to fetch dependencies  
RUN echo ':ssl_verify_mode: 0' > ~/.gemrc  
RUN gem install bundler  
RUN useradd --system --create-home --uid $PUPPET_FORGE_SERVER_USER_ID \--home-
dir $PUPPET_FORGE_SERVER_BASEDIR $PUPPET_FORGE_SERVER_USER  
  
COPY src/Gemfile Gemfile  
COPY src/Gemfile.lock Gemfile.lock  
RUN bundle --retry=3  
  
WORKDIR $PUPPET_FORGE_SERVER_BASEDIR  
USER $PUPPET_FORGE_SERVER_USER  
  
COPY src/run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  

