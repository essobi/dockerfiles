FROM naps62/nginx:latest  
MAINTAINER naps62 <mpalhas@gmail.com>  
  
# enable nginx runit services  
RUN rm -f /etc/service/nginx/down  
RUN rm -f /etc/service/nginx-log-forwarder/down  
  
# rbenv dependencies  
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) universe"  
RUN apt-get -y update  
RUN apt-get install -y build-essential curl git  
RUN apt-get install -y zlib1g-dev libssl-dev libreadline-dev libyaml-dev
libxml2-dev libxslt-dev libpq-dev  
  
# rbenv  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN ./root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/bin:/root/.rbenv/shims:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
  
# node.js  
RUN apt-get install -y nodejs npm  
  
# final cleanup  
# as specified here: https://github.com/phusion/baseimage-docker#using  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ruby  
RUN echo 'gem: --no-ri --no-rdoc' >> /.gemrc  
  
CMD ["bundle", "exec", "foreman", "start"]  

