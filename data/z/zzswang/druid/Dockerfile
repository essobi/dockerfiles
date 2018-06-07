FROM java:8  
  
MAINTAINER Dongliang He hdlmat@gmail.com  
#COPY ./druid-0.9.2-bin.tar.gz /opt/  
#COPY ./zookeeper-3.4.6.tar.gz /opt/  
COPY ./entrypoint.sh /entrypoint.sh  
RUN mkdir -p /work/csv/  
  
RUN cd /opt/ \  
&& curl "http://static.druid.io/artifacts/releases/druid-0.9.2-bin.tar.gz" -o
/opt/druid-0.9.2-bin.tar.gz \  
&& curl
"http://www.us.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz"
-o /opt/zookeeper-3.4.6.tar.gz \  
&& tar xzf druid-0.9.2-bin.tar.gz \  
&& tar xzf zookeeper-3.4.6.tar.gz \  
&& mv druid-0.9.2 druid \  
&& mv zookeeper-3.4.6 zookeeper \  
&& rm -rf *.tar.gz \  
&& gzip -c -d /opt/druid/quickstart/wikiticker-2015-09-12-sampled.json.gz >
"/opt/druid/quickstart/wikiticker-2015-09-12-sampled.json" \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& curl https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install supervisor \  
&& chmod u+x /entrypoint.sh \  
&& cd /opt/druid/ \  
&& ./bin/init  
  
  
COPY ./supervisord.conf /work/  
COPY *.sh /opt/druid/  
  
  
EXPOSE 8081  
EXPOSE 8082  
EXPOSE 8083  
EXPOSE 8090  
EXPOSE 3306  
EXPOSE 2181 2888 3888  
  
WORKDIR /work  
  
ENTRYPOINT ["/entrypoint.sh"]  

