# ベースイメージ  
FROM amazonlinux  
  
# 作成者  
MAINTAINER Gemcook, Inc <t.fujimoto@gemcook.com>  
  
# ユーザー指定  
USER root  
  
# 環境変数設定  
ENV ruby_ver="2.4.1"  
# 作業ディレクトリを指定  
WORKDIR /root  
  
# yum update  
RUN yum update -y  
  
# 共通パッケージインストール  
RUN yum install -y \  
epel-release \  
autoconf \  
curl \  
wget \  
git \  
gcc \  
gcc-c++ \  
make \  
vim \  
vi \  
emacs \  
bzip2 \  
zlib \  
readline \  
openssl \  
glibc-headers \  
sqlite \  
zlib-devel \  
bzip2-devel \  
readline-devel \  
sqlite-devel \  
mysql-devel \  
openssl-devel \  
libyaml-devel \  
kernel-devel \  
kernel-headers \  
patch \  
libyaml-devel \  
libffi-devel \  
automake \  
bison \  
tk-devel \  
zip \  
gdbm-devel \  
python-devel  
  
# Nodeインストール  
RUN curl -sL https://rpm.nodesource.com/setup_6.x | bash -  
RUN yum install -y nodejs  
  
# Yarnインストール  
RUN npm i -g yarn; yarn --version  
  
# Rubyインストール  
RUN git clone https://github.com/sstephenson/rbenv.git /usr/local/rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/usr/local/rbenv/plugins/ruby-build  
RUN echo 'export RBENV_ROOT="/usr/local/rbenv"' >> /etc/profile.d/rbenv.sh  
RUN echo 'export PATH="${RBENV_ROOT}/bin:${PATH}"' >> /etc/profile.d/rbenv.sh  
RUN echo 'eval "$(rbenv init --no-rehash -)"' >> /etc/profile.d/rbenv.sh  
RUN source /etc/profile.d/rbenv.sh; rbenv install ${ruby_ver}; rbenv global
${ruby_ver}  
RUN source /etc/profile.d/rbenv.sh; gem update --system; gem install rails;
gem install bundler  
RUN source /etc/profile.d/rbenv.sh; ruby -v  
  
# Pythonインストール  
RUN wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz  
RUN tar xzvf Python-3.6.1.tgz  
WORKDIR /root/Python-3.6.1  
RUN ./configure --with-threads  
RUN make install  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip3 install readline  
RUN pip3 install virtualenv  
RUN pip3 install django  
RUN pip3 install awscli  
  
# bashrcに記載  
RUN echo 'export RBENV_ROOT="/usr/local/rbenv"' >> /root/.bashrc  
RUN echo 'export PATH="${RBENV_ROOT}/bin:${PATH}"' >> /root/.bashrc  
RUN echo 'eval "$(rbenv init --no-rehash -)"' >> /root/.bashrc  
RUN echo 'alias la="ls -la --color"' >> /root/.bashrc  
RUN echo 'alias ll="ls -la --color"' >> /root/.bashrc  
RUN echo 'alias e="emacs "' >> /root/.bashrc  
RUN echo 'PS1_COLOR_BEGIN="\\[\e[1;36m\\]"' >> /root/.bashrc  
RUN echo 'PS1_COLOR_END="\\[\e[m\\]"' >> /root/.bashrc  
RUN echo 'export PS1="${PS1_COLOR_BEGIN}\h:\W \\\$ ${PS1_COLOR_END}"' >>
/root/.bashrc  
  
# タイムゾーンの設定  
RUN echo 'ZONE="Asia/Tokyo"' >> /etc/sysconfig/clock  
RUN echo 'UTC= true' >> /etc/sysconfig/clock  
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
WORKDIR /root  
  
CMD ["/bin/bash"]  

