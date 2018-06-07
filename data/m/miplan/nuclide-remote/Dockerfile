FROM ubuntu:16.04  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq  
  
# Install and configure SSH server  
RUN apt-get install -y gcc  
RUN apt-get install -y python-dev  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:nuclide' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Install Watchman  
RUN apt-get -y install make autoconf git libpython-dev  
RUN git clone https://github.com/facebook/watchman.git \  
&& cd watchman \  
&& git checkout v4.7.0 \  
&& ./autogen.sh \  
&& ./configure \  
&& make && make install  
  
# Install Node.js  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update -qq  
RUN apt-get install -y nodejs  
  
# Install Nuclide Remote Server  
RUN npm install -g nuclide  
  
# Install flow type  
RUN apt-get update -qq \  
&& apt-get install -y unzip libelf1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g flow-bin  
  
# Create project directory  
RUN mkdir /root/src  
WORKDIR /root/src  
  
EXPOSE 9090  
EXPOSE 2222  
# Start ssh service  
CMD ["/usr/sbin/sshd", "-D"]

