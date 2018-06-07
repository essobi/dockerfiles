FROM centos:centos7  
MAINTAINER nocsi <l@nocsi.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN yum -y update && yum -y install epel-release  
RUN yum groupinstall -y "Development Tools" && yum clean all && yum install -y
tar npm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash  
RUN ["/bin/bash", "-login", "-c", "nvm install 4.4.0"]  
RUN ["/bin/bash", "-login", "-c", "nvm use 4.4.0"]  
  
WORKDIR /engima  
RUN git clone https://github.com/NuSkooler/enigma-bbs.git .  
RUN ["/bin/bash", "-login", "-c", "npm install"]  
#RUN cd node_modules/sqlite3/lib/binding/ && mv node-v48-linux-x64
node-v46-linux-x64 && curl -o node-v46-linux-x64/node_sqlite3.node
http://www.unifieddigital.com/node_modules/sqlite3/lib/binding/node-v46-linux-x64/node_sqlite3.node  
#RUN npm install sqlite3 --build-from-source  
EXPOSE 8888  
CMD [ "/bin/bash" ]  

