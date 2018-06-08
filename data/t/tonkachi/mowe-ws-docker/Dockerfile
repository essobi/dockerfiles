FROM centos:centos6  
MAINTAINER FURUSAWA MAKOTO violafuru@gmail.com  
  
# User  
RUN adduser nes  
  
# Directories  
RUN mkdir /home/nes/.aws; chown nes:nes /home/nes/.aws ;\  
mkdir /home/nes/kumogata; chown nes:nes /home/nes/kumogata  
  
# Install tools  
RUN yum install -y git \  
openssl openssl-devel \  
pcre pcre-devel \  
zlib zlib-devel \  
libxml2 libxml2-devel libxslt-devel libffi-devel \  
readline-devel \  
gcc gcc-c++ make tar vim sudo \  
nodejs  
  
# Install psql  
RUN rpm -Uvh http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-
centos94-9.4-1.noarch.rpm ;\  
yum install -y postgresql.x86_64  
  
# Instal mysql  
RUN rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
;\  
yum --enablerepo=mysql56-community install -y mysql-community-client.x86_64  
  
# Install aws-cli  
RUN rpm -ivh http://ftp.riken.jp/Linux/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm ;\  
yum --enablerepo=epel update epel-release ;\  
yum install -y python-pip; pip install awscli  
  
ADD ./config /home/nes/.aws/config  
RUN chmod 600 /home/nes/.aws/config; chown nes:nes /home/nes/.aws/config ;\  
echo 'complete -C aws_completer aws' >> /home/nes/.bash_profile  
  
# Install rbenv and ruby-build  
USER nes  
RUN git clone https://github.com/sstephenson/rbenv.git /home/nes/.rbenv ;\  
git clone https://github.com/sstephenson/ruby-build.git
/home/nes/.rbenv/plugins/ruby-build  
ENV PATH /home/nes/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /home/nes/.bash_profile ;\  
rbenv install 2.2.2; rbenv global 2.2.2  
  
# Install bundler  
RUN echo 'gem: --no-rdoc --no-ri' >> /home/nes/.gemrc; \  
. /home/nes/.bash_profile; gem install bundler  
  
# Pull  
WORKDIR /home/nes/  
ADD ./.gitconfig /home/nes/.gitconfig  
RUN git clone https://github.com/tonkachi/ryunosu.git; \  
echo 'set number' >> /home/nes/.vimrc; \  
. /home/nes/.bash_profile; cd /home/nes/ryunosu/; bundle install --path
vendor/bundle  
  
# Run  
CMD ["/bin/bash"]  
  

