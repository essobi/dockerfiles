FROM jenkinsci/jenkins:2.96  
MAINTAINER tsukasa.tamaru<tsukasa.tamaru@2dfacto.co.jp>  
  
USER root  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y sudo gcc \  
make \  
autoconf \  
libcurl4-gnutls-dev \  
libexpat1-dev \  
gettext \  
libz-dev \  
libssl-dev  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
RUN git clone -b v2.15.1 https://github.com/git/git.git /usr/local/src/git  
RUN apt-get remove -y git  
  
WORKDIR /usr/local/src/git  
RUN make configure && \  
./configure --prefix=/usr/local && \  
make && \  
make install  
WORKDIR /var/jenkins_home  
  
RUN rm -rf /usr/local/src/git  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN groupadd docker  
RUN gpasswd -a jenkins docker  
  
USER jenkins  
  
EXPOSE 8080:8080  
EXPOSE 50000:50000  

