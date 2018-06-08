FROM centos:latest  
  
LABEL maintainer "uzresk"  
  
ARG ANSIBLE_VERSION=v2.4.0.0-1  
RUN yum -y install epel-release  
RUN yum -y install python-devel.x86_64 \  
gcc-c++ \  
gcc \  
bzip2 \  
openssl-devel \  
libyaml-devel \  
libffi-devel \  
readline-devel \  
zlib-devel \  
gdbm-devel \  
ncurses-devel \  
make \  
sshpass \  
git \  
openssl-devel  
  
# install ansible  
RUN curl -L https://bootstrap.pypa.io/get-pip.py | python && \  
pip install --upgrade pip && \  
pip install cryptography && \  
pip install git+https://github.com/ansible/ansible.git@$ANSIBLE_VERSION && \  
pip install boto && \  
pip install pywinrm  
  
# install ruby & serverspec  
ENV RBENV_ROOT /root/.rbenv  
RUN git clone https://github.com/rbenv/rbenv.git $RBENV_ROOT && \  
git clone https://github.com/sstephenson/ruby-build.git
$RBENV_ROOT/plugins/ruby-build  
ENV PATH $PATH:$RBENV_ROOT/bin:$RBENV_ROOT/shims  
RUN rbenv install 2.4.0 && \  
rbenv global 2.4.0  
RUN gem install bundler && \  
gem install serverspec \  
rspec_junit_formatter \  
winrm \  
ansible-vault \  
highline  
  

