FROM centos:latest  
  
RUN yum install -y \  
epel-release \  
openssl-devel \  
readline-devel\  
zlib-devel \  
wget \  
curl \  
httpd \  
openssh-server \  
openssh-clients \  
git \  
dtach \  
vim \  
hash-slinger \  
bzip2 \  
tar \  
libffi-devel \  
mysql \  
mysql-devel \  
libxslt-devel \  
&& yum groupinstall "Development Tools" -y \  
&& yum clean all  
  
####### begin region install ruby #######  
RUN git clone git://github.com/rbenv/rbenv.git /usr/local/rbenv \  
&& git clone git://github.com/rbenv/ruby-build.git
/usr/local/rbenv/plugins/ruby-build \  
&& git clone git://github.com/jf/rbenv-gemset.git
/usr/local/rbenv/plugins/rbenv-gemset \  
&& /usr/local/rbenv/plugins/ruby-build/install.sh  
ENV PATH /usr/local/rbenv/bin:$PATH  
ENV RBENV_ROOT /usr/local/rbenv  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh \  
&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /root/.bashrc \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /root/.bashrc \  
&& echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
  
ENV CONFIGURE_OPTS --disable-install-doc  
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH  
  
ENV RBENV_VERSION 2.4.2  
RUN eval "$(rbenv init -)"; rbenv install $RBENV_VERSION \  
&& eval "$(rbenv init -)"; rbenv global $RBENV_VERSION \  
&& eval "$(rbenv init -)"; gem update --system \  
&& eval "$(rbenv init -)"; gem install bundler -f \  
&& rm -rf /tmp/*  
####### end region install ruby #######  
# install goss
https://github.com/aelsabbahy/goss/releases/download/v0.3.5/goss-linux-386  
RUN curl -L https://github.com/aelsabbahy/goss/releases/download/v0.3.5/goss-
linux-amd64 -o /usr/local/bin/goss  
RUN chmod +rx /usr/local/bin/goss  
  
# install dgoss docker wrapper  
RUN curl -L
https://raw.githubusercontent.com/aelsabbahy/goss/v0.3.5/extras/dgoss/dgoss -o
/usr/local/bin/dgoss  
RUN chmod +rx /usr/local/bin/dgoss  
  
# create special app directory & add Ruby app & specs to it  
RUN mkdir app && cd app  
ADD ./src .  
  
# install bundler and resolve dependencies  
RUN gem install bundler  
RUN bundle install  
  
USER root  
  
ENTRYPOINT /bin/bash -l -c 'bundle exec rackup'  

