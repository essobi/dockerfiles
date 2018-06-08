from ubuntu:14.04  
maintainer James Lal [:lightsofapollo]  
  
# python is needed for many node operations (gyp)  
run apt-get install -y python  
  
ENV NODE_VERSION v0.10.33  
  
  
add http://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.gz
/tmp/node/  
run tar -C /tmp/node -zxvf /tmp/node/node* && rm /tmp/node/*.tar.gz  
run cp -R -n /tmp/node/*/* /usr/local  
run rm -Rf /tmp/node.tar.gz  
run node -v  

