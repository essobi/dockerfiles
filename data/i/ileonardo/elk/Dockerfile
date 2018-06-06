# x) - docker build -t elk/source .  
# y) - Às Instruções fica nas Dependências e no final do arquivo: [REGRA] # z)  
### Base da Imagem  
FROM ubuntu  
  
### Autor  
MAINTAINER iLeonardo Carvalho <i.leonardo.c.c@outlook.com>  
  
### Dependências  
ENV ELASTICSEARCH 2.3.4  
ENV LOGSTASH 2.3.4  
ENV KIBANA 4.5.3  
ENV JAVA 7  
ENV LOG_ROOT /opt/logs  
  
ENV ELASTICSEARCH_HOME /opt/elasticsearch  
ENV ELASTICSEARCH_CONFIG_DIRECTORY ${ELASTICSEARCH_HOME}/config  
ENV ELASTICSEARCH_CONFIG_FILE
${ELASTICSEARCH_CONFIG_DIRECTORY}/elasticsearch.yml  
ENV ELASTICSEARCH_LOG_DIRECTORY ${LOG_ROOT}/elasticsearch  
  
ENV LOGSTASH_HOME /opt/logstash  
ENV LOGSTASH_CONFIG_DIRECTORY ${LOGSTASH_HOME}/conf.d  
ENV LOGSTASH_PATTERNS_DIRECTORY ${LOGSTASH_HOME}/patterns  
ENV LOGSTASH_LOG_DIRECTORY ${LOG_ROOT}/logstash  
  
ENV KIBANA_HOME /opt/kibana  
ENV KIBANA_CONFIG_DIRECTORY ${KIBANA_HOME}/config  
ENV KIBANA_CONFIG_FILE ${KIBANA_CONFIG_DIRECTORY}/kibana.yml  
ENV KIBANA_LOG_DIRECTORY ${LOG_ROOT}/kibana  
  
# Diretório definido para executar os comandos  
WORKDIR ~/  
  
# Pacotes Essenciais  
RUN echo oracle-java${JAVA}-installer shared/accepted-oracle-license-v1-1
select true | debconf-set-selections  
  
RUN apt-get update  
RUN apt-get -qqy install software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
  
RUN apt-get update  
RUN apt-get --no-install-recommends -qqy install net-tools vim wget curl
collectd collectd-utils liboping0 oracle-java${JAVA}-installer ca-certificates
supervisor  
  
### Configurando JAVA  
ENV JAVA_HOME /usr/lib/jvm/java-${JAVA}-oracle  
ENV PATH="$PATH:${JAVA_HOME}/bin"  
RUN chmod -R 755 ${JAVA_HOME}  
RUN echo "JAVA_HOME=${JAVA_HOME}" >> /etc/environment  
RUN sed -i '/PATH/c\PATH='"'$PATH:${JAVA_HOME}/bin\'"'' /etc/environment  
  
# Executa os comandos definidos no diretório padrão  
WORKDIR /opt  
  
### Elasticsearch  
# 1) - Permissões do usuário Elasticsearch: elasticsearch  
ENV ES_GID 991  
ENV ES_UID ${ES_GID}  
  
RUN groupadd -r elasticsearch -g ${ES_GID}  
RUN useradd -r -s /usr/sbin/nologin -M -c "Elasticsearch service user" -u
${ES_UID} -g elasticsearch elasticsearch  
  
# 2) - Baixando o Código Fonte  
RUN wget
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/${ELASTICSEARCH}/elasticsearch-${ELASTICSEARCH}.tar.gz  
  
### Logstash  
# 1) - Permissões do usuário Logstash: logstash  
ENV LOGSTASH_GID 992  
ENV LOGSTASH_UID ${LOGSTASH_GID}  
  
RUN groupadd -r logstash -g ${LOGSTASH_GID}  
RUN useradd -r -s /usr/sbin/nologin -M -c "Logstash service user" -u
${LOGSTASH_UID} -g logstash logstash  
  
# 2) - Baixando o Código Fonte  
RUN wget
https://download.elastic.co/logstash/logstash/logstash-${LOGSTASH}.tar.gz  
  
### Kibana  
# 1) - Permissões do usuário Kibana: kibana  
ENV KIBANA_GID 993  
ENV KIBANA_UID ${KIBANA_GID}  
  
RUN groupadd -r kibana -g ${KIBANA_GID}  
RUN useradd -r -s /usr/sbin/nologin -M -c "Kibana service user" -u
${KIBANA_UID} -g kibana kibana  
  
# 2) - Baixando o Código Fonte  
RUN wget
https://download.elastic.co/kibana/kibana/kibana-${KIBANA}-linux-x64.tar.gz  
  
### Instalando ELK Stack  
# 1) - Criando os Diretórios  
RUN mkdir -p ${ELASTICSEARCH_HOME} ${LOGSTASH_HOME} ${KIBANA_HOME}  
RUN mkdir -p ${ELASTICSEARCH_LOG_DIRECTORY} ${LOGSTASH_LOG_DIRECTORY}
${KIBANA_LOG_DIRECTORY}  
RUN mkdir -p ${LOGSTASH_CONFIG_DIRECTORY} ${LOGSTASH_PATTERNS_DIRECTORY}  
  
# 2) - Extraindo os Códigos Fontes  
RUN tar -xzf elasticsearch*.tar.gz -C ${ELASTICSEARCH_HOME} \--strip-
components=1  
RUN tar -xzf logstash*.tar.gz -C ${LOGSTASH_HOME} \--strip-components=1  
RUN tar -xzf kibana*.tar.gz -C ${KIBANA_HOME} \--strip-components=1  
  
# 3) - Removendo os Compactados  
RUN rm *.tar.gz  
  
# 4) - Instalando o Plugin Elasticsearch kopf:
https://github.com/lmenezes/elasticsearch-kopf  
RUN ${ELASTICSEARCH_HOME}/bin/plugin install cloud-aws -b  
RUN ${ELASTICSEARCH_HOME}/bin/plugin install lmenezes/elasticsearch-kopf  
  
# 5) - Instalando o PLugin Logstash  
RUN ${LOGSTASH_HOME}/bin/logstash-plugin install logstash-input-jmx  
RUN ${LOGSTASH_HOME}/bin/logstash-plugin install logstash-filter-json  
RUN ${LOGSTASH_HOME}/bin/logstash-plugin install logstash-filter-translate  
RUN ${LOGSTASH_HOME}/bin/logstash-plugin install logstash-input-cloudwatch  
  
# 6) - Instalando o Plugin Kibana  
RUN ${KIBANA_HOME}/bin/kibana plugin --install elastic/sense  
  
# 7) - Configurações Externas  
RUN rm ${ELASTICSEARCH_CONFIG_FILE} /etc/collectd/collectd.conf  
  
ADD ./elasticsearch.yml ${ELASTICSEARCH_CONFIG_FILE}  
ADD ./kibana.yml ${KIBANA_CONFIG_FILE}  
  
ADD ./conf.d/collectd.conf ${LOGSTASH_CONFIG_DIRECTORY}  
ADD ./conf.d/logstash.conf ${LOGSTASH_CONFIG_DIRECTORY}  
  
ADD ./collectd.conf /etc/collectd/collectd.conf  
  
# LOG's  
#RUN mkdir -p /var/log/squid3/ /var/log/nginx/  
#ADD ./logs/squid.log /var/log/squid3/access.log  
#ADD ./logs/fail2ban.log /var/log/fail2ban.log  
#ADD ./patterns ${LOGSTASH_PATTERNS_DIRECTORY}  
#RUN chmod 644 /var/log/squid3/access.log /var/log/fail2ban.log
/var/log/nginx/*  
#RUN chmod 644 /var/log/squid3/access.log  
# 8) - Configurando às permissões  
RUN chmod 755 ${LOGSTASH_CONFIG_DIRECTORY}  
RUN chmod 644 ${LOGSTASH_CONFIG_DIRECTORY}/*  
  
# 9) - Dependência do 'ffi-rzmq-core' (libzmq.so)  
RUN mkdir -p /usr/local/lib && ln -s /usr/lib/*/libzmq.so.3
/usr/local/lib/libzmq.so  
  
# 10) - Executáveis do ELK para serem enxergados pelo sistema sem a
necessidade do local completo  
WORKDIR /usr/sbin  
RUN ln -sf ${ELASTICSEARCH_HOME}/bin/elasticsearch  
RUN ln -sf ${LOGSTASH_HOME}/bin/logstash  
RUN ln -sf ${KIBANA_HOME}/bin/kibana  
  
### Start  
# 1) SCRIPT executável e adaptado pelo Autor pelo comando: service
{elasticsearch | logstash | kibana} (OPTIONS)  
ADD ./init.d /etc/init.d/  
RUN chmod +x /etc/init.d/elasticsearch  
RUN chmod +x /etc/init.d/logstash  
RUN chmod +x /etc/init.d/kibana  
  
RUN update-rc.d elasticsearch defaults 95 10  
RUN update-rc.d logstash defaults 97 8  
RUN update-rc.d kibana defaults 96 9  
  
# 2) - Instalando o Supervisord para serviços em Daemon  
RUN apt-get -qqy install supervisor  
RUN mkdir -p /var/log/supervisor  
RUN touch /var/log/supervisor/supervisor.log  
ADD ./supervisor /etc/supervisor/conf.d/  
  
### Limpa os pacotes  
RUN apt-get -qqy autoremove  
RUN apt-get autoclean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /var/cache/oracle-jdk${JAVA}-installer  
  
# 3) - Expondo às configurações e logs do Elk Stack  
WORKDIR /opt  
  
# 4) - Portas necessárias  
EXPOSE 9300 9200 5000 5601  
# 5) - Arquivo inicial da execução do Docker  
CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]  
  
# z) docker run -d -p 9300:9300 -p 9200:9200 -p 5000:5000 -p 5601:5601
elk/source  

