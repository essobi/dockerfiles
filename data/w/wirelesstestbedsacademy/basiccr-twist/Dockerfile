FROM ubuntu:14.04  
MAINTAINER "Mikolaj Chwalisz" <chwalisz@tkn.tu-berlin.de>  
  
LABEL Description="This image is used to work with TinyOS" Vendor="CREW"
Version="1.0"  
  
# TinyOS toolchain  
# It was created following http://tinyos.stanford.edu/tinyos-
wiki/index.php/Automatic_installation  
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys A9B913B9  
RUN gpg -a --export A9B913B9 | apt-key add -  
  
RUN echo "deb http://tinyprod.net/repos/debian wheezy main" >>
/etc/apt/sources.list.d/tinyprod-debian.list  
RUN echo "deb http://tinyprod.net/repos/debian msp430-46 main" >>
/etc/apt/sources.list.d/tinyprod-debian.list  
  
RUN apt-get update  
RUN apt-get install -y nesc tinyos-tools-devel gcc-msp430  
  
# Other packages  
RUN apt-get install -y git-core build-essential  
RUN apt-get install -y python-pip python-dev libxml2-dev libxslt1-dev libz-dev  
RUN apt-get install -y screen tmux  
  
RUN locale-gen en_US.UTF-8  
  
# SSH  
RUN apt-get install -y openssh-server sudo  
RUN useradd --create-home --shell /bin/bash wta  
RUN echo 'wta ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/10-wta-sudo  
RUN mkdir -p /var/run/sshd  
  
RUN echo "wta:crew" | chpasswd  
  
EXPOSE 22  
# TinyOS  
RUN git clone \--depth=1 https://github.com/tinyos/tinyos-main.git
/home/wta/tinyos-main  
RUN chown wta:wta -R /home/wta/tinyos-main  
  
ENV TINYOS_ROOT_DIR="/home/wta/tinyos-main"  
ENV CLASSPATH=$CLASSPATH:$TINYOS_ROOT_DIR/support/sdk/java  
ENV PYTHONPATH=$PYTHONPATH:$TINYOS_ROOT_DIR/support/sdk/python  
ENV HOME=/home/wta  
  
# Wireless Testbed Academy  
ADD . /home/wta/BasicCR  
RUN chown wta:wta -R /home/wta/BasicCR  
  
RUN pip install -r /home/wta/BasicCR/requirements.txt  
  
WORKDIR /home/wta/BasicCR  
USER wta  
  
CMD /usr/sbin/sshd -D  

