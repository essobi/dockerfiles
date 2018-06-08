FROM repositoryjp/centos:6.7  
MAINTAINER Shinya Kinoshita <skinoshita@repositories.jp>  
  
LABEL name="Python Version Management (pyenv) v20160422 Image" \  
description="The image for creating docker container of Python Version
Management (pyenv) v20160422." \  
distribution="centos" \  
centos-version="6.7" \  
pyenv-version="v20160422" \  
vendor="REPOSITORY <http://www.repositories.jp>" \  
license="MIT"  
  
ENV pyenv_version 20160422  
USER root  
WORKDIR /usr/local/src  
  
# Install necessary packages.  
RUN yum install -y readline-devel \  
zlib-devel \  
openssl-devel \  
sqlite-devel  
  
# Install pyenv.  
RUN wget https://github.com/yyuu/pyenv/archive/v${pyenv_version}.tar.gz && \  
tar xvzf v${pyenv_version}.tar.gz && \  
mv pyenv-${pyenv_version} pyenv && \  
rm -f v${pyenv_version}.tar.gz && \  
echo 'export PYENV_ROOT="/usr/local/src/pyenv"' >> /etc/profile.d/pyenv.sh &&
\  
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /etc/profile.d/pyenv.sh && \  
echo 'eval "$(pyenv init -)"' >> /etc/profile.d/pyenv.sh && \  
exec $SHELL -l && \  
pyenv --version  
  
# Configure container  
USER root  
WORKDIR /root  
  
CMD ["/usr/sbin/sshd", "-D"]  

