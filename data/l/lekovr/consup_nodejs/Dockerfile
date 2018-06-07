# consup nodejs  
# node.js v6  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_baseapp  
  
ENV DOCKERFILE_VERSION 161116  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs bzip2 libfontconfig1  
  
#
-------------------------------------------------------------------------------  
# user op  
RUN useradd -m -r -s /bin/bash -Gwww-data -gusers -gsudo op  
  
#
-------------------------------------------------------------------------------  
# Extra libs  
COPY package.json /home/op  
RUN cd /home/op \  
&& chown op /usr/lib/node_modules \  
&& ln -s /usr/lib/node_modules node_modules \  
&& npm install --only=dev  
  
#
-------------------------------------------------------------------------------  
# Consup  
COPY init.sh /  
CMD ["/init.sh"]  
  
WORKDIR /home/app  
  
ENV APPUSER op  
  

