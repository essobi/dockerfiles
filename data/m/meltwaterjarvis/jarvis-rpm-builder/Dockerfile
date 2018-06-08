FROM centos:6  
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
ENV LANGUAGE=en_US.UTF-8  
RUN yum -y install epel-release rpm-build  
  
WORKDIR /root  
  
# Install ruby stuff  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby=1.9.3  
RUN bash -l -c 'source /usr/local/rvm/scripts/rvm && gem install --no-ri --no-
rdoc package_cloud json:1.8.3 fpm:1.4'  
  
# install npm stuff  
RUN yum -y install npm && npm i -g npm@2.14.9  
ADD ./root /root  
  
ENTRYPOINT ["bash", "-l", "-c", "~/build.sh"]  

