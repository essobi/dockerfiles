FROM ubuntu-debootstrap:trusty  
MAINTAINER Anthony Powles  
  
# install tools and dependencies  
RUN apt-get -y update && apt-get -qy --no-install-recommends install \  
ca-certificates \  
curl \  
git \  
mysql-client \  
redis-tools \  
sudo \  
tmux \  
vim \  
\  
build-essential \  
libmysqlclient-dev \  
libffi-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
\  
&& apt-get clean  
  
# install rbenv  
ENV RBENV_ROOT /opt/rbenv  
ENV PATH $RBENV_ROOT/bin:$RBENV_ROOT/shims:$PATH  
  
RUN git clone https://github.com/sstephenson/rbenv.git ${RBENV_ROOT} \  
&& git clone https://github.com/sstephenson/ruby-build.git
${RBENV_ROOT}/plugins/ruby-build \  
\  
&& echo 'export RBENV_ROOT=/opt/rbenv' >> /etc/profile.d/rbenv.sh \  
&& echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh \  
&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh \  
&& chmod +x /etc/profile.d/rbenv.sh \  
\  
&& echo "install: --no-rdoc --no-ri\nupdate: --no-rdoc --no-ri" > /etc/gemrc  
  

