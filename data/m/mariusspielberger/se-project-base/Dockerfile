#start with elastic as base  
FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.0  
USER root  
  
RUN printf "123\n123" | passwd root  
  
#copy configs  
ADD kibana.repo /etc/yum.repos.d/  
  
RUN rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch  
RUN echo y | yum install logstash-5.5.0-1 kibana-5.5.0-1
freetype-2.4.11-12.el7 fontconfig-2.10.95-10.el7 fontpackages-
filesystem-1.44-8.el7  
  
RUN curl -sLO https://nodejs.org/dist/v6.11.0/node-v6.11.0-linux-x64.tar.xz &&
tar xf node-v6.11.0-linux-x64.tar.xz && mv node-v6.11.0-linux-x64
/usr/share/node && rm -f node-v6.11.0-linux-x64.tar.xz  
  
RUN chown --recursive elasticsearch:elasticsearch /usr/share/kibana/
/var/lib/kibana/ /usr/share/logstash/ /usr/share/node  
RUN ln -s /usr/share/node/bin/node /usr/bin/node  
RUN ln -s /usr/share/node/bin/npm /usr/bin/npm  
RUN chmod 0777 /usr/bin/node /usr/bin/npm  
  
RUN npm install node-red@0.16.2  
  
ADD settings.js /usr/share/elasticsearch/node_modules/node-red/  
RUN chown elasticsearch: /usr/share/elasticsearch/node_modules/node-
red/settings.js  
  
EXPOSE 1880  
USER elasticsearch  
  
CMD /bin/bash

