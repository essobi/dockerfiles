# Yeoman with some generators and prerequisites  
FROM debian:jessie  
  
MAINTAINER Josh Cox <josh@webhosting.coop>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install node.js, then npm install yo and the generators  
RUN apt-get -yq update && \  
apt-get -yq install git curl net-tools sudo bzip2 libpng-dev locales-all  
RUN apt-get install -yq libavahi-compat-libdnssd-dev vim keychain  
  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \  
apt-get -yq install nodejs  
  
RUN npm install -g npm && \  
npm install -g yo bower grunt-cli gulp && \  
npm install -g generator-webapp generator-angular generator-gulp-angular \  
npm install -g generator-jekyllrb generator-jekyllized  
  
# Add a yeoman user because grunt doesn't like being root  
RUN adduser --uid 1000 --disabled-password --gecos "" yeoman && \  
echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Expose the port  
EXPOSE 9000  
# set HOME so 'npm install' and 'bower install' don't write to /  
ENV HOME /home/yeoman  
  
ENV LANG en_US.UTF-8  
RUN mkdir /src && chown yeoman:yeoman /src  
WORKDIR /src  
  
ADD set_env.sh /usr/local/sbin/  
RUN chmod +x /usr/local/sbin/set_env.sh  
ENTRYPOINT ["set_env.sh"]  
  
# Always run as the yeoman user  
USER yeoman  
  
# RVM install ruby  
RUN ["/bin/bash", "-c", "gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3"]  
RUN ["/bin/bash", "-c", "curl -L get.rvm.io | bash -s stable"]  
RUN ["/bin/bash", "-c", "echo 'source /home/yeoman/.rvm/scripts/rvm
'>>~/.bashrc"]  
RUN ["/bin/bash", "-c", "source /home/yeoman/.rvm/scripts/rvm ; rvm
requirements; rvm install ruby-2.1.4; rvm use --default 2.1.4; source
/home/yeoman/.rvm/scripts/rvm"]  
RUN ["/bin/bash", "-c", "source /home/yeoman/.rvm/scripts/rvm ; rvm use
--default 2.1.4; gem install bundler"]  
# install SPF13 vim  
RUN ["/bin/bash", "-c", "curl http://j.mp/spf13-vim3 -L -o - | sh"]  
  
CMD /bin/bash  

