FROM centos:7  
MAINTAINER michimau <mauro.michielon@eea.europa.eu>  
  
RUN yum -y install epel-release  
RUN yum -y update  
RUN yum -y install npm git curl vim nodejs  
  
RUN npm install -g n  
  
ENV KIBANA_VERSION 6.2.4  
RUN git clone https://github.com/elastic/kibana.git /kibana-dev \  
&& cd /kibana-dev \  
&& git checkout v$KIBANA_VERSION  
  
RUN sed "s#Loading Kibana##g" -i /kibana-
dev/src/core_plugins/kibana/translations/en.json  
RUN sed "s#title Kibana#title EEA#g" -i /kibana-
dev/src/ui/ui_render/views/chrome.jade  
  
ADD src/ui_app.jade /tmp/ui_app.jade  
  
RUN sed -i -e '/\\.kibanaWelcomeLogo {/{r /tmp/ui_app.jade' -e 'd}' /kibana-
dev/src/ui/ui_render/views/ui_app.jade \  
&& rm /tmp/ui_app.jade  
  
ADD src/*.png /kibana-dev/src/ui/public/assets/favicons/  
ADD src/*.ico /kibana-dev/src/ui/public/assets/favicons  
ADD src/*.svg /kibana-dev/src/ui/public/assets/favicons  
  
WORKDIR /kibana-dev  
RUN n "$(cat .node-version)"  
RUN npm install  
  
RUN npm run build --skip-os-packages --force  
  
RUN mv /kibana-dev/build/kibana-$KIBANA_VERSION-SNAPSHOT-linux-x86_64
/opt/kibana  
  
RUN sed "s#-SNAPSHOT##g" -i /opt/kibana/package.json  
  
RUN cp /opt/kibana/config/kibana.yml /opt/kibana.yml  
  
RUN rm -rf /kibana-dev  
  
ENV PATH /opt/kibana/bin:$PATH  
  
ADD docker-entrypoint.sh /  
RUN chmod a+x /docker-entrypoint.sh  
  
EXPOSE 5601  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/opt/kibana/bin/kibana"]  

