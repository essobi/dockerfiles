FROM debian:jessie  
MAINTAINER Thibault Coupin <thibault.coupin@gmail.com>  
  
RUN apt-get update && apt-get install -y python2.7 libpython2.7 python-
setuptools python-imaging python-ldap sqlite3  
RUN mkdir /seafile  
WORKDIR /seafile  
ADD https://bintray.com/artifact/download/seafile-org/seafile/seafile-
server_5.0.4_x86-64.tar.gz /  
RUN tar -zxvf /seafile-server*5.0.4_x86-64.tar.gz && ln -s seafile-
server-5.0.4 seafile-server-latest  
  
ADD workspace/ ./  
ADD start.sh ./  
RUN chmod +x start.sh  
  
CMD ./start.sh && tail -f /seafile/logs/seahub.log  

