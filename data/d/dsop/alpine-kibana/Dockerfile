FROM dsop/alpine-nodejs  
  
ENV KIBANA_VERSION 5.1.1-linux-x86_64  
ENV KIBANA_UID 1000  
RUN mkdir /opt && \  
cd /opt && \  
curl -L
https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}.tar.gz
-o kibana-${KIBANA_VERSION}.tar.gz && \  
tar xzf kibana-${KIBANA_VERSION}.tar.gz && \  
ln -s kibana-${KIBANA_VERSION} kibana && \  
rm -rf kibana/node && \  
ln -s /opt/kibana/bin/kibana /usr/local/bin/  
  
RUN adduser -u ${KIBANA_UID} -D kibana -s /bin/bash  
RUN cp /root/.bashrc /home/kibana && \  
chown -R ${KIBANA_UID}:${KIBANA_UID} /home/kibana  
  
USER kibana  
WORKDIR /home/kibana  
  
EXPOSE 5601  
ENTRYPOINT ["kibana", "-H", "0.0.0.0", "-e" ]  

