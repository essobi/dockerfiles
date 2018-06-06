FROM centos:7  
RUN yum -y update \  
&& yum -y install unzip wget sudo lsof telnet bind-utils tar tcpdump vim
sysstat strace less  
RUN yum install -y epel-release  
RUN yum install -y mongodb-server mongodb  
RUN mkdir -p /var/lib/mongodb && chown -R mongodb:mongodb /var/lib/mongodb  
RUN systemctl enable mongod  
ENV HOME /root  
WORKDIR ${HOME}  
RUN echo "export TERM=xterm" >> .bash_profile  
ENV NODEJS_VERSION=v8.5.0  
RUN wget -qO -
https://nodejs.org/dist/${NODEJS_VERSION}/node-${NODEJS_VERSION}-linux-x64.tar.xz
| tar xf - -C /usr/local -J \  
&& ln -s /usr/local/node-${NODEJS_VERSION}-linux-x64 /usr/local/nodejs  
RUN wget -qO - https://github.com/chip-in/dadget/archive/master.tar.gz | tar
zxf -  
WORKDIR ${HOME}/dadget-master/examples/server  
ENV PATH $PATH:/usr/local/nodejs/bin  
RUN npm install && npm run build  
COPY dadget.service /usr/lib/systemd/system/  
RUN systemctl enable dadget  
CMD ["/sbin/init"]

