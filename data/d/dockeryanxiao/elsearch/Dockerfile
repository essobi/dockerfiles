From ingensi/oracle-jdk  
RUN wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.6.9.tar.gz
-P /usr/local  
RUN yum -y install tar  
RUN tar xzvf /usr/local/elasticsearch-5.6.9.tar.gz -C /usr/local  
COPY elasticsearch.yml /usr/local/elasticsearch-5.6.9/config/  
RUN echo "elsearch soft nofile 65536" >>/etc/security/limits.conf  
RUN echo "elsearch hard nofile 131072" >>/etc/security/limits.conf  
RUN echo "elsearch soft nproc 2048" >> /etc/security/limits.conf  
RUN echo "elsearch hard nproc 4096" >>/etc/security/limits.conf  
RUN groupadd elsearch  
RUN useradd elsearch -g elsearch  
RUN sed -i s/2g/1g/g /usr/local/elasticsearch-5.6.9/config/jvm.options  
RUN chown elsearch:elsearch /usr/local/elasticsearch-5.6.9  
RUN usermod elsearch -G root  
RUN mkdir -p /da/es/data  
RUN mkdir -p /da/es/logs  
RUN mkdir -p /usr/local/elasticsearch-5.6.9/config/scripts  
RUN chown -R elsearch:elsearch /da/es  
USER elsearch  
WORKDIR /usr/local/elasticsearch-5.6.9/bin  
CMD [ "sh", "-x", "elasticsearch" ]  

