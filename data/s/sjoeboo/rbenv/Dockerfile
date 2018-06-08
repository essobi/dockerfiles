FROM centos:7  
RUN yum -y install git gcc gcc-c++ make git bzip2 openssl-devel readline-devel
zlib-devel curl-devel && yum clean all  
  
RUN useradd -m -d /home/ruby -p ruby ruby && chsh -s /bin/bash ruby  
USER ruby  
RUN git clone https://github.com/sstephenson/rbenv.git /home/ruby/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/home/ruby/.rbenv/plugins/ruby-build  
#RUN /home/ruby/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /home/ruby/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /home/ruby/.bashrc  
ENV CONFIGURE_OPTS --disable-install-doc  
RUN echo 'gem: --no-rdoc --no-ri' >> /home/ruby/.gemrc  
  
ENV HOME /home/ruby  
ENV PATH
/home/ruby/.rbenv/shims:/home/ruby/.rbenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN rbenv install 2.3.1  
RUN rbenv global 2.3.1  
RUN gem install bundler  

