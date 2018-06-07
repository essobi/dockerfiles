FROM java:8u66-jre  
MAINTAINER tsukasa.tamaru<tsukasa.tamaru@2dfacto.co.jp>  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y openssh-server \  
sudo \  
gcc \  
make \  
autoconf \  
libcurl4-gnutls-dev \  
libexpat1-dev \  
gettext \  
libz-dev \  
libssl-dev \  
git \  
expect  
  
RUN git clone -b v2.6.3 https://github.com/git/git.git /usr/local/src/git  
RUN apt-get remove -y git  
  
WORKDIR /usr/local/src/git  
RUN make configure && \  
./configure --prefix=/usr/local && \  
make && \  
make install  
WORKDIR /var/jenkins_home  
  
RUN rm -rf /usr/local/src/git  
  
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN mkdir -p /var/run/sshd  
  
RUN adduser --quiet jenkins  
RUN echo "jenkins:jenkins" |chpasswd  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

