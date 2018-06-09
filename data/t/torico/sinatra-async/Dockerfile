# docker file for 'sinatra-async'  
FROM centos:latest  
MAINTAINER yamada@torico.co  
WORKDIR /root  
ENV HOME /root  
ENV PATH "/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"  
# set up MySQL 5.6 (Global Transaction ID enabled)  
COPY docker/*.rpm /root/  
RUN yum localinstall -y MySQL-shared-compat-5.6.25-1.el7.x86_64.rpm  
RUN yum localinstall -y MySQL-shared-5.6.25-1.el7.x86_64.rpm  
RUN yum localinstall -y MySQL-devel-5.6.25-1.el7.x86_64.rpm  
RUN yum localinstall -y MySQL-client-5.6.25-1.el7.x86_64.rpm  
  
# install middlewares.  
RUN yum -y update  
RUN yum install -y epel-release  
RUN yum install -y which tar curl wget bzip2  
RUN yum install -y automake autoconf libtool  
RUN yum install -y subversion patch bison  
RUN yum install -y glibc-devel glibc-headers gcc-c++  
RUN yum install -y readline-devel zlib-devel sqlite-devel  
RUN yum install -y openssl-devel libffi-devel  
RUN yum install -y libyaml libyaml-devel  
RUN yum install -y libxml2 libxml2-devel  
RUN yum install -y libxslt libxslt-devel  
  
# install rvm, ruby, bundler into /usr/local/rvm.  
ENV LANG ja_JP.UTF-8  
RUN curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -  
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby=2.2.2  
RUN bash -l -c "rvm requirements"  
RUN source /usr/local/rvm/scripts/rvm  
ENV PATH "/usr/local/rvm/bin:${PATH}"  
RUN bash -l -c "rvm --default use 2.2.2"  
RUN bash -l -c "gem install bundler --no-ri --no-rdoc"  
RUN bash -l -c "gem install rake --no-ri --no-rdoc"  
RUN echo "source /usr/local/rvm/scripts/rvm" >> /etc/bashrc  
RUN echo "rvm --default use 2.2.2" >> /etc/bashrc  
  
# install app to /root  
ENV PATH "${GEM_HOME}/bin:${PATH}"  
RUN bash -l -c "[ -d /root/log ] || mkdir /root/log"  
RUN bash -l -c "[ -d /root/public ] || mkdir /root/public"  
ADD . /root/  
ADD docker/thin.yml /root/  
ADD docker/Gemfile /root/  
RUN bash -l -c "bundle install"  
  
# start thin server as entrypoint.  
EXPOSE 3001  
ADD docker/thin_proc.sh /root/thin_proc.sh  
RUN chmod +x /root/thin_proc.sh  
CMD /root/thin_proc.sh  
  

