FROM debian:latest  
MAINTAINER rainereduardolopez@gmail.com  
  
# use rbenv understandable version  
ARG RUBY_VERSION  
ENV RUBY_VERSION=${RUBY_VERSION:-2.4.0}  
  
ENV RBENV_ROOT /usr/local/share/rbenv  
ENV RUBY_BUILD_PATH $RBENV_ROOT/plugins/ruby-build  
  
ENV PATH $PATH:$RBENV_ROOT/bin  
  
RUN useradd -ms /bin/bash pikeman && \  
useradd -ms /bin/bash deploy  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y autoconf \  
bison \  
build-essential \  
curl \  
git \  
libffi-dev \  
libgdbm-dev \  
libgdbm3 \  
libncurses5-dev \  
libreadline6-dev \  
libssl-dev \  
libyaml-dev \  
zlib1g-dev \  
runit \  
rubygems-integration  
  
RUN mkdir -p $RBENV_ROOT && \  
chown -R deploy:deploy $RBENV_ROOT  
  
USER deploy  
  
RUN git clone \--depth 1 https://github.com/rbenv/rbenv.git $RBENV_ROOT  
RUN git clone \--depth 1 https://github.com/rbenv/ruby-build.git
$RUBY_BUILD_PATH  
  
RUN export CONFIGURE_OPTS="--disable-install-doc" && \  
eval "$(rbenv init -)" && \  
rbenv install $RUBY_VERSION && \  
rbenv global $RUBY_VERSION && \  
rbenv rehash  
  
RUN eval "$(rbenv init -)" && \  
gem update --system && \  
gem update && \  
gem install fakes3 -v 0.2.5  
  
USER root  
  
# SSH  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
#CMD ["/usr/sbin/sshd", "-D"]  
USER root  
  
# CLEAN  
RUN apt-get autoremove -y && \  
apt-get clean  
  
# RUNIT FOLDERS (SERVICES)  
RUN mkdir -p /etc/sv/nginx && \  
mkdir -p /etc/sv/nginx/log && \  
mkdir -p /etc/sv/pikeman && \  
mkdir -p /etc/sv/pikeman/log && \  
mkdir -p /etc/sv/fakes3 && \  
mkdir -p /etc/sv/fakes3/log && \  
mkdir -p /etc/sv/postgres && \  
mkdir -p /etc/sv/postgres/log  
  
ADD scripts/nginx/run /etc/sv/nginx/  
ADD scripts/nginx/log/run /etc/sv/nginx/log  
ADD scripts/pikeman/run /etc/sv/pikeman  
ADD scripts/pikeman/log/run /etc/sv/pikeman/log  
ADD scripts/fakes3/run /etc/sv/fakes3  
ADD scripts/fakes3/down /etc/sv/fakes3  
ADD scripts/fakes3/log/run /etc/sv/fakes3/log  
  
RUN ln -nsf /etc/sv/nginx /etc/service/ && \  
ln -nsf /etc/sv/pikeman /etc/service/ && \  
ln -nsf /etc/sv/fakes3 /etc/service/ && \  
ln -nsf /etc/sv/fakes3 /etc/service/  
  
CMD /usr/sbin/sshd -D && ls -l

