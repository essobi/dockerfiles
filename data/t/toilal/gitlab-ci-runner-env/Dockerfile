FROM sameersbn/gitlab-ci-runner  
MAINTAINER toilal.dev@gmail.com  
  
RUN apt-get update  
  
# Install build-essential for C/C++ support  
RUN apt-get install -y build-essential  
  
USER gitlab_ci_runner  
  
# Install nvm for nodeJS support  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash  
  
# Installing nodeJS  
RUN bash -c ". ~/.nvm/nvm.sh &&\  
nvm install 0.10 &&\  
nvm install 0.11 &&\  
nvm install iojs"  
  
# Install rbenv for Ruby support  
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv &&\  
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.profile &&\  
echo 'eval "$(rbenv init -)"' >> ~/.profile  
  
# Install rbenv install command  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
  
# Install requirements to compile ruby  
USER root  
RUN apt-get install -y git-core curl zlib1g-dev build-essential\  
libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3\  
libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties  
# Additional dependency for ruby 2.2.0  
RUN apt-get install -y libffi-dev  
USER gitlab_ci_runner  
  
# Install Ruby  
RUN . ~/.profile &&\  
rbenv install 1.9.3-p551 &&\  
rbenv install 2.0.0-p598 &&\  
rbenv install 2.1.5 &&\  
rbenv install 2.2.0  
  
# Install pyenv  
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv &&\  
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile &&\  
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile  
  
# Installing requirements to compile Python  
USER root  
RUN apt-get build-dep -y python2.7 python3.4  
USER gitlab_ci_runner  
  
# Install Python  
RUN . ~/.profile && pyenv install 2.7.9 &&\  
pyenv install 3.3.6 &&\  
pyenv install 3.4.2 &&\  
pyenv install pypy-2.4.0 &&\  
pyenv install pypy3-2.4.0  
  
# Install Oracle JDK (Java)  
USER root  
RUN apt-get install -y software-properties-common  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections &&\  
add-apt-repository -y ppa:webupd8team/java &&\  
apt-get update  
  
RUN apt-get install -y oracle-java6-installer && rm -rf /var/cache/oracle-
jdk6-installer  
RUN apt-get install -y oracle-java7-installer && rm -rf /var/cache/oracle-
jdk7-installer  
RUN apt-get install -y oracle-java8-installer && rm -rf /var/cache/oracle-
jdk8-installer  
  
# Install Maven and Ant  
RUN apt-get install -y maven ant  
  
# Install jenv  
USER gitlab_ci_runner  
RUN git clone https://github.com/gcuisinier/jenv.git ~/.jenv &&\  
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.profile &&\  
echo 'eval "$(jenv init -)"' >> ~/.profile  
  
# Register JDK into jenv  
RUN bash -c ". ~/.profile &&\  
jenv add /usr/lib/jvm/java-6-oracle &&\  
jenv add /usr/lib/jvm/java-7-oracle &&\  
jenv add /usr/lib/jvm/java-8-oracle"  
  
# Go back to root  
USER root  
  
# Cleanup apt lists  
RUN rm -rf /var/lib/apt/lists/*

