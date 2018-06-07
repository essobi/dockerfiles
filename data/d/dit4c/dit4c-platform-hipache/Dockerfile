# DOCKERFILE 1.1.0  
FROM dit4c/dit4c-platform-base  
MAINTAINER t.dettrick@uq.edu.au  
  
# Install NPM  
RUN yum install -y nodejs tar git gcc-c++ && \  
curl -L https://npmjs.org/install.sh | clean=no sh  
  
# Install Hipache  
RUN git clone -b 0.3.1 https://github.com/hipache/hipache.git /opt/hipache &&
\  
cd /opt/hipache && \  
npm install  
  
ADD /etc /etc  
  
EXPOSE 8080  
CMD ["/opt/hipache/bin/hipache", "--config", "/etc/hipache.json"]  

