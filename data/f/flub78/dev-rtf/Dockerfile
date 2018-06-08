# Ruby development and test container  
#  
# FROM ubuntu:14.04  
FROM ubuntu  
  
MAINTAINER Frédéric Peignot frederic.peignot@free.fr  
  
RUN apt-get update \  
&& apt-get install -y openssh-server \  
python \  
python-apt \  
git \  
vim \  
gcc \  
make \  
rake \  
ruby-dev \  
libffi-dev \  
libtcltk-ruby \  
libx11-dev \  
tcl-dev tk-dev \  
apache2 \  
libmysqlclient-dev \  
mysql-client \  
inetutils-ping \  
gedit \  
sudo  
  
RUN gem update --system  
RUN gem install watir  
RUN gem install minitest  
RUN gem install minitest-ci  
RUN gem install dbi  
RUN gem install tk  
RUN gem install dbd-mysql  
  
RUN mkdir /var/run/sshd  
  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config;  
  
EXPOSE 22  
RUN mkdir /root/.ssh/  
# Copy over private key, and set permissions  
# ADD id_rsa /root/.ssh/id_rsa  
# Create known_hosts  
RUN touch /root/.ssh/known_hosts  
# Add github key  
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
RUN useradd -m dev && echo "dev:dev" | chpasswd && adduser dev sudo  
  
ENV HOME /home/dev  
  
RUN (cd /home/dev; git clone https://github.com/flub78/rtf.git)  
  
# CMD ["/usr/sbin/sshd", "-D"]  
# CMD ["/usr/sbin/apache2ctl", "-D FOREGROUND"]  
ENTRYPOINT service ssh restart && \  
/usr/sbin/apache2ctl -D FOREGROUND  
  
# USER dev  

