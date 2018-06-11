FROM google/nodejs:latest  
MAINTAINER Jordan Li  
RUN apt-get update -y  
RUN apt-get install -y -q python-software-properties  
RUN apt-get install -y -q python  
RUN apt-get install -y -q python-dev  
RUN apt-get install -y -q python-distribute  
RUN apt-get install -y -q python-pip  
RUN \  
echo "# Install OpenSSH Server" ;\  
apt-get -q -y install openssh-server ;\  
mkdir -p /var/run/sshd ;\  
echo 'root:passw0rd' | chpasswd ;\  
\  
true  
RUN npm install -g node-gyp  
RUN npm install -g codebox  
  
# Rebuild pty.js  
# codebox cannot find module ../build/Release/pty.node if don't rebuild pty.js  
# http://stackoverflow.com/questions/23570023/issues-in-finding-node-package-
when-running-codebox  
RUN cd /nodejs/lib/node_modules/codebox/node_modules/shux/node_modules/pty.js
\  
&& make clean && make  
  
RUN mkdir -p /workspace  
WORKDIR /workspace  
EXPOSE 8000  
ENTRYPOINT ["/nodejs/bin/codebox", "run"]  

