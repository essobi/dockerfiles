FROM opensuse/leap  
  
MAINTAINER emni  
  
ENV OMNIDB_VERSION 2.8.0  
RUN zypper ref  
RUN zypper -n up  
  
RUN zypper -n in curl unzip make python3-pip wget llvm  
RUN zypper -n in libopenssl-devel readline-devel sqlite3-devel zlib-devel
libbz2-devel xz  
RUN zypper -n in \--type pattern devel_basis  
  
RUN curl -Lo /tmp/OmniDB.zip
https://github.com/OmniDB/OmniDB/archive/${OMNIDB_VERSION}.zip  
RUN unzip /tmp/OmniDB.zip -d /opt/  
RUN rm -f /tmp/OmniDB.zip  
RUN cd /opt/OmniDB-${OMNIDB_VERSION} && pip3 install pip --upgrade && pip3
install cherrypy && pip3 install -r requirements.txt  
  
RUN mkdir -p /data  
  
EXPOSE 8080  
EXPOSE 25482  
WORKDIR /opt/OmniDB-${OMNIDB_VERSION}/OmniDB  
  
CMD python3 omnidb-server.py -d /data -p 8080  

