FROM centos:centos7  
MAINTAINER makky <makky.4d6b.3f5@gmail.com>  
  
RUN rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-
centos-7-0.el7.ngx.noarch.rpm  
RUN rpm -ivh http://ftp.riken.jp/Linux/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# update epel-release  
RUN yum remove -y epel-release  
RUN yum install -y epel-release  
  
# packages install  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y epel-release git ruby-devel nodejs npm openssl openssl-
devel readline readline-devel zlib-devel libffi-devel  
  
# nginx install  
RUN yum install -y nginx --enablerepo=nginx  
RUN rm /usr/share/nginx/html/*  
  
# rbenv install  
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile  
RUN echo 'export LC_CTYPE="en_US.UTF-8"' >> ~/.bash_profile  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
  
# ruby install  
RUN source ~/.bash_profile && rbenv install 2.2.0 && rbenv global 2.2.0 &&
rbenv rehash  
  
# gem install  
RUN source ~/.bash_profile && rbenv exec gem install bundler  
RUN source ~/.bash_profile && rbenv exec bundle config --global jobs 4  
  
# clone repository  
RUN git clone https://github.com/makky3939/blog.makky.io.git  
  
# build app  
RUN source ~/.bash_profile && cd blog.makky.io && rbenv exec bundle instal  
RUN source ~/.bash_profile && cd blog.makky.io && rbenv exec jekyll build  
RUN cp -r blog.makky.io/_site/* /usr/share/nginx/html/  
  
# port open  
EXPOSE 80  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

