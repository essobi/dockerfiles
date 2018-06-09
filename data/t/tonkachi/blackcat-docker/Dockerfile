FROM centos:centos7  
MAINTAINER FURUSAWA MAKOTO violafuru@gmail.com  
  
ENV APP blackcat  
ENV RUBY_VERSION 2.2.3  
# Install packages for building ruby  
RUN yum install -y epel-release  
RUN yum install -y git \  
openssl openssl-devel \  
pcre pcre-devel \  
zlib zlib-devel \  
libxml2 libxml2-devel libxslt-devel \  
readline-devel \  
gcc make tar \  
nodejs sqlite3 sqlite-devel  
  
RUN adduser michiru  
RUN mkdir /apps  
RUN chown michiru:michiru /apps  
  
# Install rbenv and ruby-build  
USER michiru  
RUN git clone https://github.com/sstephenson/rbenv.git /home/michiru/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/home/michiru/.rbenv/plugins/ruby-build  
ENV PATH /home/michiru/.rbenv/bin:$PATH  
RUN echo 'export PATH=${HOME}/.rbenv/bin:${PATH}' >>
/home/michiru/.bash_profile; \  
echo 'eval "$(rbenv init -)"' >> /home/michiru/.bash_profile; \  
rbenv install ${RUBY_VERSION}; \  
rbenv global ${RUBY_VERSION};  
  
# Install bundler  
RUN echo 'gem: --no-rdoc --no-ri' >> /home/michiru/.gemrc  
RUN . /home/michiru/.bash_profile; gem install bundler  
  
# git clone app  
WORKDIR /apps/  
RUN git clone https://github.com/tonkachi/${APP}.git ${APP}  
WORKDIR /apps/${APP}  
RUN . /home/michiru/.bash_profile; \  
bundle install --path vendor/bundle --without development test; \  
bundle exec rake db:migrate RAILS_ENV=production;  
  
# Run  
EXPOSE 80  
EXPOSE 443  
USER root  
RUN ln -s /home/michiru/.rbenv /root/.rbenv  
ADD ./rails_wrapper.sh /home/michiru/rails_wrapper.sh  
RUN chown michiru:michiru /home/michiru/rails_wrapper.sh && chmod 755
/home/michiru/rails_wrapper.sh  
  
CMD ["/home/michiru/rails_wrapper.sh", "michiru", "blackcat"]  

