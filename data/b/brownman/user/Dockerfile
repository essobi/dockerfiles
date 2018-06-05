# pgolm/docker-gitlab-ci-runner  
  
FROM brownman/apt  
#ubuntu:12.10  
MAINTAINER pgolm "golm.peter@gmail.com"  
  
RUN echo "gitlab_ci_runner ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN service sudo restart  
  
  
  
# Config  
#ENV INSTALL_RUBY_VERSION 2.1.0  
  
# apt-get deps  
#RUN apt-get update -y  
#RUN apt-get install -y -q sudo wget git build-essential libicu-dev \  
# lsb-release software-properties-common tklib zlib1g-dev libssl-dev \  
# libreadline-gplv2-dev libxml2 libxml2-dev libxslt1-dev  
  
#RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) main universe restricted multiverse"  
  
# switch priveleges  
RUN adduser --disabled-login --gecos 'GitLab CI Runner' gitlab_ci_runner  
USER gitlab_ci_runner  
ENV HOME /home/gitlab_ci_runner  
#RUN echo gitlab_ci_runner:gitlab_ci_runner | chpasswd  
# install ruby, bundler  
#RUN wget -qO - https://raw.github.com/fesplugas/rbenv-
installer/master/bin/rbenv-installer | bash  
#ENV RBENV_ROOT ${HOME}/.rbenv  
#ENV PATH ${RBENV_ROOT}/bin:${PATH}  
  
#RUN rbenv install $INSTALL_RUBY_VERSION  
#RUN rbenv global $INSTALL_RUBY_VERSION  
#RUN echo "eval \"\$(rbenv init -)\"" >> $HOME/.profile  
#RUN . $HOME/.profile && gem install bundler  
  
# install gitlab-ci-runner  
  
WORKDIR /home/gitlab_ci_runner  
  
# prepare SSH  
RUN mkdir -p $HOME/.ssh  
RUN echo 'echo "-------------------------> loading $HOME/.bashrc"' >>
$HOME/.bashrc  
  
#RUN git clone \--depth=1 https://github.com/gitlabhq/gitlab-ci-runner.git
runner  
# Jan 02, 2014  
#ENV RUNNER_REVISION 08f2260ae87e101f72194a27229b249d126e35fe  
#RUN cd runner && git checkout $RUNNER_REVISION && . $HOME/.profile && bundle
install  
  
#CMD cd $HOME/runner  
#CMD . ../.profile && ssh-keyscan -H $GITLAB_SERVER_FQDN >>
$HOME/.ssh/known_hosts && bundle exec ./bin/setup_and_run  

