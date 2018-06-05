FROM centos:7  
MAINTAINER "Johandry Amador" <johandry@gmail.com>  
  
ENV IMAGE_NAME johandry/devsecops  
ENV IMAGE_VERSION 0.1.3  
# Ruby Version to install  
ENV RUBY_VER 2.3.1  
# For Python source, use the .tar.xz file.  
ENV PYTHON_2 http://www.python.org/ftp/python/2.7.11/Python-2.7.11.tar.xz  
ENV PYTHON_3 http://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz  
  
# Non-root user  
ENV REG_USER devsecops  
  
# Install base packages and NodeJS  
RUN yum install -y epel-release \  
gcc \  
make \  
perl \  
curl \  
curl-devel \  
wget \  
bzip2 \  
tar \  
patch \  
net-tools \  
git \  
vim \  
xz-libs \  
sudo \  
nfs-utils \  
links \  
lynx \  
nodejs  
  
# Installing Python 2 & 3 (AWS CLI requirement) and pip  
RUN cd /tmp && \  
wget ${PYTHON_2} -O /tmp/Python-2.tar.xz && \  
wget ${PYTHON_3} -O /tmp/Python-3.tar.xz && \  
tar xf Python-2.tar.xz && rm -f Python-2.tar.xz && \  
tar xf Python-3.tar.xz && rm -f Python-3.tar.xz && \  
cd /tmp/Python-2* && ./configure && make && make install && \  
cd /tmp/Python-3* && ./configure && make && make install && \  
cd /tmp && \  
rm -rf /tmp/Python-2* && \  
rm -rf /tmp/Python-3* && \  
yum install -y python-pip && \  
pip install --upgrade pip  
  
# Install AWS CLI  
RUN pip install awscli  
  
# Instal Penetration Test Tools  
RUN yum install -y nmap \  
libpcap-devel \  
postgresql-devel \  
libsqlite3-dev \  
sqlite-devel && \  
curl https://raw.githubusercontent.com/rapid7/metasploit-
omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb >
/tmp/msfinstall && \  
chmod 755 /tmp/msfinstall && \  
/tmp/msfinstall && \  
rm -f /tmp/msfinstall  
  
# Installing Ruby dependencies  
RUN yum install -y autoconf \  
bison \  
openssl-devel \  
expat-devel \  
gettext-devel \  
readline-devel \  
gcc-c++ \  
zlib-devel && \  
echo 'export PATH="/home/${REG_USER}/.rbenv/bin:$PATH"' >
/etc/profile.d/rbenv-path-setup.sh && \  
echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv-path-setup.sh  
  
RUN yum clean all  
  
# Create non-root user  
RUN useradd -m ${REG_USER} && \  
echo "${REG_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/vagrant  
  
# The following instructions are required to be executed as a non-root user.  
USER ${REG_USER}  
WORKDIR /home/${REG_USER}  
ENV HOME /home/${REG_USER}  
  
# Installing Ruby and required gems  
RUN git clone https://github.com/rbenv/rbenv.git /home/${REG_USER}/.rbenv && \  
git clone https://github.com/rbenv/ruby-build
/home/${REG_USER}/.rbenv/plugins/ruby-build && \  
echo -ne "install: --no-document\nupdate: --no-document\ngem: --no-document"
>> "$HOME/.gemrc" && \  
/bin/bash --login -c "rbenv install ${RUBY_VER} && rbenv global ${RUBY_VER}"
&& \  
/bin/bash --login -c "gem install bundler rails" && \  
chown -R ${REG_USER}.${REG_USER} /home/${REG_USER}/.rbenv  
  
# Install Assumer (DevSecOps Toolkit)  
RUN mkdir -p /home/${REG_USER}/toolkit && \  
cd $_ && \  
git clone https://github.com/devsecops/assumer && \  
/bin/bash --login -c "cd /home/${REG_USER}/toolkit/assumer/source && gem build
assumer.gemspec && gem install assumer-*.gem"  
  
# Install Restacker (DevSecOps Toolkit)  
RUN mkdir -p /home/${REG_USER}/toolkit && \  
cd $_ && \  
git clone https://github.com/devsecops/restacker && \  
/bin/bash --login -c "cd /home/${REG_USER}/toolkit/restacker/source && bundle
&& gem build restacker.gemspec && gem install restacker-*.gem"  
  
# Install Selfie (DevSecOps Toolkit)  
RUN mkdir -p /home/${REG_USER}/toolkit && \  
cd $_ && \  
git clone https://github.com/devsecops/selfie && \  
/bin/bash --login -c "cd /home/${REG_USER}/toolkit/selfie && bundle && gem
build selfie.gemspec && gem install selfie-*.gem"  
  
# Login to the container as soon as it run  
CMD ["/bin/bash","--login"]  

