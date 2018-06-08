FROM ubuntu:14.04  
# Init ENV  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen it_IT.UTF-8  
ENV LANG it_IT.UTF-8  
ENV LANGUAGE it  
ENV LC_ALL it_IT.UTF-8  
ENV KETTLE_VERSION 5.0.1-stable  
ENV KETTLE_TAG 5.0.1-stable  
  
ENV PENTAHO_HOME /opt/pentaho  
  
# Install Updates, Dependencies and Oracle JDK 7  
RUN apt-get update && apt-get install zip netcat curl wget unzip vim python-
software-properties software-properties-common postfix sharutils mailutils
postgresql-client dnsutils -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Apply JAVA_HOME  
ENV PENTAHO_JAVA_HOME $JAVA_HOME  
ENV PENTAHO_JAVA_HOME /opt/pentaho/jdk1.7.0_79  
ENV JAVA_HOME /opt/pentaho/jdk1.7.0_79  
  
RUN mkdir ${PENTAHO_HOME}; useradd -s /bin/bash -d ${PENTAHO_HOME} pentaho;
chown pentaho:pentaho ${PENTAHO_HOME}  
  
USER pentaho  
  
RUN mkdir -p ${PENTAHO_HOME}/.kettle ${PENTAHO_HOME}/setup
${PENTAHO_HOME}/functions ${PENTAHO_HOME}/jdk1.7.0_79  
  
COPY jdk1.7.0_79 ${PENTAHO_HOME}/jdk1.7.0_79  
# Data Integration con librerie customizzate Extra  
COPY data-integration ${PENTAHO_HOME}/data-integration  
# Trasformazione kettle per cifratura password + script creazione file
repositories.xml parametrizzato  
COPY ./repositories_xml.ktr ${PENTAHO_HOME}/setup/repositories_xml.ktr  
COPY ./create_repo.sh ${PENTAHO_HOME}/setup/create_repo.sh  
# Modello file kettle.properties  
COPY ./kettle.properties ${PENTAHO_HOME}/.kettle/kettle.properties  
# Script di sostituzione delle variabili acquisite all'avvio  
COPY ./sed_env_var.sh ${PENTAHO_HOME}/setup/sed_env_var.sh  
# Script di update dell'ip di ElasticSearch  
COPY ./update_ip.sh ${PENTAHO_HOME}/setup/update_ip.sh  
# Script di scambio dei DB a caricamento validato  
COPY ./alter_db.sh ${PENTAHO_HOME}/setup/alter_db.sh  
COPY ./alter_db_ko.txt ${PENTAHO_HOME}/setup/alter_db_ko.txt  
# Script trasformazioni kettle per caricamenti notturni  
COPY scripts_trasformazioni ${PENTAHO_HOME}/setup/scripts_trasformazioni  
# Script di orchestrazione all'avvio, richiama gli altri script  
COPY ./setup.sh ${PENTAHO_HOME}/setup/setup.sh  
# Funzioni  
COPY functions ${PENTAHO_HOME}/functions  
  
USER root  
RUN echo "pentaho ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN chown -R pentaho:pentaho ${PENTAHO_HOME}  
  
USER pentaho  
  
WORKDIR ${PENTAHO_HOME}  
  
CMD ["/bin/bash", "/opt/pentaho/setup/setup.sh"]  

