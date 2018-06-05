# compass image  
# runs compass within a container  
FROM centos:centos7  
MAINTAINER François Zaninotto <francois+docker@marmelab.com>  
  
ENV HOME /root  
  
RUN yum -y update  
  
# set default umask to 002  
ADD ./root/etc/profile /etc/profile  
ADD ./root/docker-umask-wrapper.sh /bin/docker-umask-wrapper.sh  
#ADD ./root/etc/sysctl.conf /etc/sysctl.conf  
# install ruby  
RUN yum -y install ruby tar make ca-certificates gpg gcc ruby-devel rubygems  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
  
#RUN gem uninstall sass  
#RUN gem uninstall compass  
#RUN \curl -sSL https://get.rvm.io | bash -s stable  
RUN curl -L get.rvm.io | bash -s stable  
RUN source /etc/profile.d/rvm.sh  
RUN /usr/local/rvm/bin/rvm install ruby-2.1.2  
RUN gem install sass --pre  
RUN gem install compass --pre  
  
# install compass  
#RUN gem install --no-rdoc --no-ri compass  
#RUN echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf &&
sudo sysctl -p  
RUN chmod u+x /bin/docker-umask-wrapper.sh  
RUN mkdir /src  
WORKDIR /src  
  
CMD docker-umask-wrapper.sh compass watch  

