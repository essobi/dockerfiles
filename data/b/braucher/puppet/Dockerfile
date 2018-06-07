# base Ubuntu image with puppet and puppet-related tools  
FROM ubuntu-upstart:14.04  
MAINTAINER Jeff Braucher <jeff@braucher.net>  
  
ENV PUPPET_VERSION '~>3'  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# Fix terminal settings on ubuntu image  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Fix terminal for the root user  
RUN echo 'export TERM=xterm' >> ~/.bashrc  
  
# Fix initctl on ubuntu image (hard-coded to 1.12.1 to go with Ubuntu 14.04)  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN echo '#!/bin/bash\nif [ $1 == "--version" ]\nthen\n echo "initctl (upstart
1.12.1)"\nfi\n/bin/true' > /sbin/initctl  
RUN chmod 755 /sbin/initctl  
  
# compilers and ruby  
RUN apt-get update && apt-get install -y \  
make \  
software-properties-common \  
apt-transport-https \  
ruby \  
ruby-dev \  
git  
  
# puppet  
RUN gem install --no-ri --no-rdoc \  
\--version "${PUPPET_VERSION}" puppet  
  
# puppet tools  
RUN gem install --no-ri --no-rdoc \  
deep_merge \  
librarian-puppet  
  
# puppet-apply, default manifests, default hiera  
COPY ./puppet-apply /  
COPY ./puppet/ /puppet-default/  
ENV PUPPET_HOME /puppet-default  
ENTRYPOINT /puppet-apply  

