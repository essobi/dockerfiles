FROM fedora:24  
MAINTAINER Michael Clayton <mclayton@redhat.com>  
  
ENV LANG en_US.utf8  
  
RUN dnf update -y  
RUN dnf groupinstall -y development-tools rpm-development-tools c-development  
RUN dnf install -y git nodejs npm ruby ruby-devel  
RUN dnf clean all  
  
RUN gem update --system  
RUN gem install sass compass breakpoint toolkit git-up  
  
RUN npm install -g grunt-cli bower  

