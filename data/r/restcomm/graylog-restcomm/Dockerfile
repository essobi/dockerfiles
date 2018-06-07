FROM graylog2/server:2.0.3-2  
RUN apt-get update \  
&& apt-get install -y wget  
  
COPY ./ConfigureGraylog.sh /etc/my_init.d/configureGraylog.sh  
RUN chmod +x /etc/my_init.d/configureGraylog.sh  
  
COPY ./Template_ContentPack.json /opt/graylog/contentpacks/  
COPY ./LoadBalancer_ContentPack.json /opt/graylog/contentpacks/  
  
ADD https://github.com/sivasamyk/graylog2-plugin-input-
httpmonitor/releases/download/v1.0.3/graylog2-plugin-input-
httpmonitor-1.0.3.jar opt/graylog/plugin/  
  
RUN mkdir -p /opt/graylog/sv/index  
COPY ./result_template.sh /opt/graylog/sv/index/run  
RUN chmod +x /opt/graylog/sv/index/run  
  

