FROM centos:centos7  
MAINTAINER FURUSAWA MAKOTO m.furusawa@gmail.com  
  
# Install packages for building ruby  
RUN yum install -y epel-release  
RUN yum install -y git \  
openssl openssl-devel \  
pcre pcre-devel \  
zlib zlib-devel \  
libxml2 libxml2-devel libxslt-devel \  
readline-devel \  
gcc make tar \  
postgresql.x86_64 postgresql-devel.x86_64 \  
nodejs  
  
RUN adduser michiru  
RUN mkdir /apps  
RUN chown michiru:michiru /apps  
  
# Install nginx  
RUN mkdir /apps/src  
WORKDIR /apps/src  
RUN curl -O http://nginx.org/download/nginx-1.7.6.tar.gz ;\  
tar zxvf nginx-1.7.6.tar.gz  
WORKDIR /apps/src/nginx-1.7.6  
RUN ./configure --prefix=/apps/nginx --with-http_ssl_module --with-
http_spdy_module ;\  
make; make install  
  
# Install rbenv and ruby-build  
USER michiru  
RUN git clone https://github.com/sstephenson/rbenv.git /home/michiru/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/home/michiru/.rbenv/plugins/ruby-build  
ENV PATH /home/michiru/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /home/michiru/.bash_profile  
RUN rbenv install 2.0.0-p481  
RUN rbenv global 2.0.0-p481  
  
# Install bundler  
RUN echo 'gem: --no-rdoc --no-ri' >> /home/michiru/.gemrc  
RUN . /home/michiru/.bash_profile; gem install bundler  
  
# git clone app  
WORKDIR /apps/  
RUN git clone https://github.com/tonkachi/woodpecker.git woodpecker  
WORKDIR /apps/woodpecker  
RUN . /home/michiru/.bash_profile; \  
bundle install --path vendor/bundle --without development test;  
  
# rails_wrapper  
ADD ./rails_wrapper.sh /home/michiru/rails_wrapper.sh  
ADD ./michiru_part.sh /home/michiru/michiru_part.sh  
USER root  
RUN chown michiru:michiru /home/michiru/rails_wrapper.sh && chmod 755
/home/michiru/rails_wrapper.sh; \  
chown michiru:michiru /home/michiru/michiru_part.sh && chmod 755
/home/michiru/michiru_part.sh  
  
# Run  
EXPOSE 80  
EXPOSE 443  
RUN rm /apps/nginx/conf/nginx.conf; ln -s /apps/woodpecker/config/nginx.conf
/apps/nginx/conf/nginx.conf  
WORKDIR /home/michiru/  
CMD /home/michiru/rails_wrapper.sh  

