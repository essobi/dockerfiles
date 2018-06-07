# Docker container with metasploit.  
#  
# Use Kali the latest Kali Linux base image  
#FROM linux/kali  
FROM kalilinux/kali-linux-docker  
MAINTAINER David Mitchell "david.mitchell@digital-shokunin.net"  
EXPOSE 443  
ADD ./init.sh /init.sh  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean  
  
RUN echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-
free" >> /etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean  
  
RUN bash -c 'echo "deb http://mirrors.aliyun.com/kali kali main" >
/etc/apt/sources.list'  
RUN apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6  
  
# Install metasploit  
RUN apt-get -y update ; apt-get -y --force-yes install debian-archive-keyring
kali-archive-keyring libnokogiri-ruby metasploit-framework curl debian-
archive-keyring kali-archive-keyring  
  
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -  
RUN curl -L https://get.rvm.io -o rvm-install.sh  
RUN chmod +x rvm-install.sh  
RUN ./rvm-install.sh  
RUN source /usr/local/rvm/src/rvm/scripts/rvm  
RUN touch /root/.bashrc  
RUN echo 'source /usr/local/rvm/src/rvm/scripts/rvm' >> /root/.bashrc  
RUN source /root/.bashrc  
RUN /usr/local/rvm/bin/rvm install 2.1.5  
RUN /usr/local/rvm/bin/rvm use 2.1.5 --default  
RUN rm -f /usr/local/bin/rake  
RUN ln -s /usr/local/rvm/src/ruby-2.1.5/bin/rake /usr/local/bin/rake  
RUN rm -f /usr/bin/ruby  
RUN ln -s /usr/local/rvm/src/ruby-2.1.5/ruby /usr/bin/ruby  
  
ENV HOME="/root"  
# Attach this container to stdin when running, like this:  
# docker run -t -i linux/kali/metasploit  
CMD ["/init.sh;","/bin/bash"]  

