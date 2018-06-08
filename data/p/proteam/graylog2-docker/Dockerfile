FROM sjoerdmulder/java8  
  
# Install pwgen and add authorized keys  
RUN apt-get install -y pwgen  
# Add mongodb repo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/mongodb.list  
RUN apt-get update  
  
VOLUME ["/data"]  
  
# Install mongodb  
RUN apt-get install -y mongodb-org-server mongodb-org-shell mongodb-org-tools  
  
# Install elasticsearch  
RUN wget -O - -o /dev/null
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.1.tar.gz
| tar -xz -C /opt  
RUN ln -s /opt/elasticsearch-1.4.1 /opt/elasticsearch  
  
RUN useradd -s /bin/false -r -M elasticsearch  
  
# Get graylog2 server  
RUN wget -O - -o /dev/null
http://packages.graylog2.org/releases/graylog2-server/graylog2-server-0.92.4.tgz
| tar -xz -C /opt  
RUN ln -s /opt/graylog2-server-0.92.4 /opt/graylog2-server  
  
RUN useradd -s /bin/false -r -M graylog2  
# Setup server config  
ADD etc/graylog2.conf /etc/graylog2.conf  
RUN sed -i -e "s/password_secret =$/password_secret = $(pwgen -s 96)/"
/etc/graylog2.conf  
  
# Get the web-interface  
RUN wget -O - -o /dev/null http://packages.graylog2.org/releases/graylog2-web-
interface/graylog2-web-interface-0.92.4.tgz | tar -xz -C /opt  
RUN ln -s /opt/graylog2-web-interface-0.92.4 /opt/graylog2-web-interface  
  
# Setup the web-interface  
RUN sed -i -e "s/application.secret=.*$/application.secret=\"$(pwgen -s
96)\"/" /opt/graylog2-web-interface/conf/graylog2-web-interface.conf  
RUN sed -i -e
"s/graylog2-server.uris=.*$/graylog2-server.uris=\"http:\/\/127.0.0.1:12900\/\"/"
/opt/graylog2-web-interface/conf/graylog2-web-interface.conf  
  
RUN chown graylog2:root /opt/graylog2-server-0.92.4 /opt/graylog2-web-
interface-0.92.4  
# Expose ports  
# - 9000: Web interface  
# - 12201: GELF UDP  
# - 12900: REST API  
EXPOSE 9000 12201/udp 12900  
ADD mongo-configuration.js /tmp/mongo-configuration.js  
ADD service /etc/service  
  

