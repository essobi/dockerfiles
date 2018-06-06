FROM debian:8  
# Install puppet  
RUN apt-get -y update  
RUN apt-get -y install curl wget git rubygems  
RUN curl -Ls https://raw.github.com/cargomedia/puppet-
packages/master/scripts/puppet-install.sh | bash  
RUN gem install --no-ri --no-rdoc librarian-puppet  
  
# SSH identity for GitHub  
RUN mkdir -p /root/.ssh  
ADD ssh/cargomedia-anonymous /root/.ssh/id_rsa  
RUN chmod 600 /root/.ssh/id_rsa  
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config  

