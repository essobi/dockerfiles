FROM fedora  
ENV MBSE_ROOT=/opt/mbse  
  
RUN mkdir -p /docker  
  
RUN dnf -y install \  
darkhttpd \  
findutils \  
gcc \  
git \  
iproute \  
make \  
mgetty \  
ncurses-devel \  
net-tools \  
openssh-server \  
passwd \  
procps-ng \  
python-pip \  
supervisor \  
tar \  
telnet-server \  
unzip \  
vim \  
xinetd \  
zip \  
zlib-devel  
  
RUN mkdir -p /src  
WORKDIR /src  
RUN git clone https://git.code.sf.net/p/mbsebbs/code mbsebbs-code  
WORKDIR /src/mbsebbs-code  
  
COPY build-mbse.sh /docker/build-mbse.sh  
RUN sh /docker/build-mbse.sh  
  
COPY create-users.sh /docker/create-users.sh  
RUN sh /docker/create-users.sh  
  
COPY install-mbse.sh /docker/install-mbse.sh  
RUN sh /docker/install-mbse.sh  
  
COPY xinetd.d /etc/xinetd.d  
  
WORKDIR $MBSE_ROOT  
EXPOSE 23 80 24554 60177 60179  
COPY entrypoint.sh /docker/entrypoint.sh  
ENTRYPOINT ["sh", "/docker/entrypoint.sh"]  
  
COPY supervisord.d /etc/supervisord.d/  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-n"]  
  
COPY python-mbse /root/python-mbse  
RUN cd /root/python-mbse; pip install .  

