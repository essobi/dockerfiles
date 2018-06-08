FROM centos:latest  
  
RUN yum install -y \  
git \  
tar vim \  
gcc gcc-c++ make patch \  
libxslt-devel libxml2-devel libcurl-devel mysql-devel readline-devel \  
hostname nmap-ncat; \  
yum -y clean all  
  
# install ruby 2  
RUN git clone https://github.com/sstephenson/ruby-build.git /root/ruby-build
&& /root/ruby-build/install.sh  
RUN ruby-build 2.2.3 /ruby  
  
RUN echo "export PATH=$PATH:/ruby/bin" > /etc/profile.d/ruby.sh  
ENV PATH $PATH:/ruby/bin  
  
RUN gem install -N bundler  
  
RUN yum install -y \  
epel-release; \  
yum -y clean all  
  
RUN yum install -y \  
nodejs npm; \  
yum -y clean all  
  
RUN yum install -y \  
wget sudo; \  
yum -y clean all  
  
RUN curl https://toolbelt.heroku.com/install.sh > /heroku-installer.sh  
RUN sed -i "s/sudo //g" /heroku-installer.sh  
RUN sed -i "s/-k//g" /heroku-installer.sh  
RUN chmod +x /heroku-installer.sh  
RUN ./heroku-installer.sh  
  
RUN echo "export PATH=$PATH:/usr/local/heroku/bin" > /etc/profile.d/heroku.sh  
ENV PATH $PATH:/usr/local/heroku/bin  
  
RUN heroku  
RUN mkdir /app  
WORKDIR /app  
  
RUN gem sources --remove https://rubygems.org/  
RUN gem sources --add https://ruby.taobao.org/  
  
RUN gem install rails  
  
RUN bundle config 'mirror.https://rubygems.org' 'https://ruby.taobao.org'  
  
RUN yum install -y sqlite-devel.x86_64  
RUN yum install -y postgresql postgresql-devel  
  
COPY . /app  
  
RUN bundle  
  
ENTRYPOINT ["/bin/bash"]  

