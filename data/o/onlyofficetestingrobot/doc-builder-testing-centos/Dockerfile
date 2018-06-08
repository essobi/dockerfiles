FROM centos:latest  
  
MAINTAINER Pavel.Lobashov "shockwavenn@gmail.com"  
RUN yum -y install https://github.com/feedforce/ruby-
rpm/releases/download/2.4.0/ruby-2.4.0-1.el7.centos.x86_64.rpm  
RUN yum -y install git gcc make file-devel zlib-devel google-crosextra-
carlito-fonts ImageMagick-devel which  
RUN gem install bundler  
COPY . /doc-builder-testing  
WORKDIR /doc-builder-testing  
RUN /bin/bash -l -c 'bundle install --without development'  
RUN rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x8320CA65CB2DE8E5"  
RUN echo $'[documentbuilder] \n\  
name = onlyoffice-documentbuilder \n\  
baseurl = http://download.onlyoffice.com/repo/centos/main/noarch/ \n\  
enabled = 1 \n\  
gpgcheck = 1' > /etc/yum.repos.d/documentbuilder.repo  
RUN yum -y install onlyoffice-documentbuilder  
CMD /bin/bash -l -c "[ ! -z \"$UPDATE_DOCUMENTBUILDER\" ] && yum clean all &&
yum -y update onlyoffice-documentbuilder; \  
onlyoffice-documentbuilder; \  
cd /doc-builder-testing; \  
bundle update; \  
bundle exec parallel_rspec spec"  

