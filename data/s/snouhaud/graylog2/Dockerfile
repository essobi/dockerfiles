FROM snouhaud/java7:latest  
  
# Install pwgen and add authorized keys  
RUN apt-get install -y pwgen  
# Add mongodb repo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/mongodb.list  
RUN apt-get update  
  
RUN echo 'Europe/Paris' | tee /etc/timezone  
  
VOLUME ["/data"]  
  
# Install mongodb  
RUN apt-get install -y mongodb-org-server  
  
# Install elasticsearch  
RUN wget -O - -o /dev/null
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.4.tar.gz
| tar -xz -C /opt  
RUN ln -s /opt/elasticsearch-1.3.4 /opt/elasticsearch  
  
RUN useradd -s /bin/false -r -M elasticsearch  
  
# Get graylog2 server  
RUN wget -O - -o /dev/null
http://packages.graylog2.org/releases/graylog2-server/graylog2-server-0.91.1.tgz
| tar -xz -C /opt  
RUN ln -s /opt/graylog2-server-0.91.1 /opt/graylog2-server  
  
RUN useradd -s /bin/false -r -M graylog2  
# Setup server config  
ADD etc/graylog2.conf /etc/graylog2.conf  
RUN sed -i -e "s/password_secret =$/password_secret = $(pwgen -s 96)/"
/etc/graylog2.conf  
  
# Get the web-interface  
RUN wget -O - -o /dev/null http://packages.graylog2.org/releases/graylog2-web-
interface/graylog2-web-interface-0.91.1.tgz | tar -xz -C /opt  
RUN ln -s /opt/graylog2-web-interface-0.91.1 /opt/graylog2-web-interface  
  
# Setup the web-interface  
RUN sed -i -e "s/application.secret=.*$/application.secret=\"$(pwgen -s
96)\"/" /opt/graylog2-web-interface/conf/graylog2-web-interface.conf  
RUN sed -i -e
"s/graylog2-server.uris=.*$/graylog2-server.uris=\"http:\/\/127.0.0.1:12900\/\"/"
/opt/graylog2-web-interface/conf/graylog2-web-interface.conf  
  
#RUN mkdir -p /etc/service/graylog2-server/spool  
RUN chown -R graylog2:root /opt/graylog2-server-0.91.1 /opt/graylog2-web-
interface-0.91.1  
# Expose ports  
# - 9000: Web interface  
# - 12201: GELF UDP  
# - 12202: TCP1  
# - 12203: TCP2  
# - 12204: TCP3  
# - 12205: TCP4  
# - 12206: UDP1  
# - 12207: UDP2  
# - 12208: UDP3  
# - 12209: UDP4  
# - 12900: REST API  
# - 22: SSH  
EXPOSE 22 9000 12201/udp 12202 12203 12204 12205 12206/udp 12207/udp 12208/udp
12209/udp  
  
ADD service /etc/service  

