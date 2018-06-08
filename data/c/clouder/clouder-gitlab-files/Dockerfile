FROM clouder/clouder-base  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -qq
install git build-essential zlib1g-dev libyaml-dev libssl-dev libpq-dev
libgdbm-dev libreadline-dev libncurses5-dev libffi-dev curl openssh-server
checkinstall libxml2-dev libxslt-dev libcurl4-openssl-dev libicu-dev logrotate
python-docutils pkg-config cmake nodejs ruby ruby-dev golang  
  
RUN useradd -d /home/git -s /bin/bash git  
RUN mkdir /home/git  
RUN chown git:git /home/git  
  
RUN mkdir -p /opt/gitlab/files  
RUN chown -R git:git /opt/gitlab  
  
# Clone GitLab repository  
RUN cd /opt/gitlab/files  
RUN git clone https://gitlab.com/gitlab-org/gitlab-ce.git /opt/gitlab/files -b
8-11-stable  
  
RUN gem install bundler --no-ri --no-rdoc  
RUN cd /opt/gitlab/files; bundle install --deployment --without development
test mysql aws kerberos  
  
RUN git clone https://gitlab.com/gitlab-org/gitlab-workhorse.git
/opt/gitlab/gitlab-workhorse  
RUN cd /opt/gitlab/gitlab-workhorse; git checkout v0.7.8  
RUN cd /opt/gitlab/gitlab-workhorse; make  
  
RUN ln -s /opt/gitlab/config/gitlab.yml /opt/gitlab/files/config/gitlab.yml  
RUN ln -s /opt/gitlab/config/secrets.yml /opt/gitlab/files/config/secrets.yml  
RUN ln -s /opt/gitlab/config/resque.yml /opt/gitlab/files/config/resque.yml  
RUN ln -s /opt/gitlab/config/database.yml
/opt/gitlab/files/config/database.yml  
RUN ln -s /opt/gitlab/config/unicorn.rb /opt/gitlab/files/config/unicorn.rb  
RUN ln -s /opt/gitlab/config/rack_attack.rb
/opt/gitlab/files/config/initializers/rack_attack.rb  
  
RUN rm -rf /opt/gitlab/files/log  
RUN rm -rf /opt/gitlab/files/tmp  
RUN rm -rf /opt/gitlab/files/public/uploads  
RUN rm -rf /opt/gitlab/files/builds  
RUN rm -rf /opt/gitlab/files/shared/artifacts  
RUN ln -s /opt/gitlab/var/log /opt/gitlab/files/log  
RUN ln -s /opt/gitlab/var/tmp /opt/gitlab/files/tmp  
RUN ln -s /opt/gitlab/data/uploads /opt/gitlab/files/public/uploads  
RUN ln -s /opt/gitlab/data/builds /opt/gitlab/files/builds  
RUN ln -s /opt/gitlab/data/artifacts /opt/gitlab/files/shared/artifacts  
  
RUN chown -R git:git /opt/gitlab  

