From centos:7  
MAINTAINER "takemi.ohama" <takemi.ohama@ietty.co.jp>  
  
RUN yum -y update && yum -y upgrade  
RUN yum install -y '@Development Tools'  
RUN yum install -y epel-release  
RUN yum install -y wget subversion git sudo bzip2  
RUN yum install -y openssl-devel readline-devel zlib-devel curl-devel \  
libyaml-devel libffi-devel ImageMagick ImageMagick-devel ipa-pgothic-fonts  
RUN yum install -y mariadb mariadb-devel mariadb-libs  
RUN yum clean all  
RUN sed -i -e "s/Defaults requiretty/#Defaults requiretty/" /etc/sudoers  
  
WORKDIR /usr/local  
RUN git config --global credential.helper store  
  
RUN git clone https://github.com/sstephenson/rbenv.git rbenv  
RUN mkdir rbenv/shims rbenv/versions rbenv/plugins  
RUN groupadd rbenv && chgrp -R rbenv rbenv && chmod -R g+rwxXs rbenv  
  
WORKDIR /usr/local/rbenv/plugins  
RUN git clone git://github.com/sstephenson/ruby-build.git ruby-build  
RUN chgrp -R rbenv ruby-build && chmod -R g+rwxs ruby-build  
  
RUN git clone git://github.com/sstephenson/rbenv-default-gems.git rbenv-
default-gems  
RUN chgrp -R rbenv rbenv-default-gems && chmod -R g+rwxs rbenv-default-gems  
  
RUN echo 'export RBENV_ROOT="/usr/local/rbenv"' > /etc/profile.d/rbenv.sh  
RUN echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
RUN echo 'bundler' >> /usr/local/rbenv/default-gems  
RUN echo 'rbenv-rehash' >> /usr/local/rbenv/default-gems  
RUN echo '%rbenv ALL=(ALL) ALL' >> /etc/sudoers  
ENV PATH "/usr/local/rbenv/shims:/usr/local/rbenv/bin:$PATH"  
RUN source /etc/profile.d/rbenv.sh  
RUN ruby-build/install.sh  
ENV CONFIGURE_OPTS --disable-install-doc  
  
RUN su -l root -c 'rbenv install 2.3.0 -v'  
RUN su -l root -c 'rbenv rehash'  
RUN su -l root -c 'rbenv global 2.3.0'  
  
RUN adduser docker  
RUN usermod -G rbenv,wheel,users docker  
RUN usermod -G users root  
RUN echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
EXPOSE 3000  
USER docker  
WORKDIR /home/docker  
  
CMD ["tail","-f","/dev/null"]  

