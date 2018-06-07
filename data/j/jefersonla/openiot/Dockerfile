# OpenIoT Dockerfile by WiserUFBA Research Group  
# ---------------------------------------------------------------------------  
# Created by Jeferson Lima  
# At Universidade Federal da Bahia  
# Project SmartUFBA  
# Version 1.0.0  
# Description:  
# This is the default dockerfile for deploy OpenIoT Application with docker.  
# It's already totally configured, and prepared for integration with X-GSN,  
# Which you should do it manually after the deploy.  
#  
# Descricao:  
# Esse é o Dockerfile de instalação de um container OpenIoT  
# totalmente configurado. O objetivo deste container é o de  
# se tornar o modelo padrão de deploy da aplicação OpenIoT  
# ---------------------------------------------------------------------------  
FROM ubuntu:14.04  
MAINTAINER Jeferson Lima <jefersonlimaa@dcc.ufba.br>  
  
# 1 Passo - Preparação do ambiente  
# ---------------------------------------------------------------------------  
# Para nossa primeira execução iremos utilizar a versão 14.04 do ubuntu  
# Como em 'https://github.com/OpenIotOrg/openiot/wiki/Installation-Guide'  
# precisamos configurar algumas variavéis de ambiente para a correta  
# execução do OpenIoT  
# Step 1 - Environment Preparation  
# ---------------------------------------------------------------------------  
# This step will configure with the environment used by OpenIoT Application  
# it consists of Ubuntu Linux 14.04 with Maven 3.0, Java 7 and Latest Virtuoso  
# release.  
# You can change OpenIoT branch here if you wanna, by default the OpenIoT  
# Branch selected is the development branch, but you can change this.  
# Como em 'https://github.com/OpenIotOrg/openiot/wiki/Installation-Guide'  
# precisamos configurar algumas variavéis de ambiente para a correta  
# execução do OpenIoT  
# Home das Aplicações necessárias  
# ---------------------------------------------------------------------------  
# Home of the applications needed  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV MAVEN_HOME /usr/share/maven3  
ENV VIRTUOSO_HOME /usr/local/virtuoso-opensource  
ENV JBOSS_HOME /opt/jboss  
ENV OPENIOT_HOME /opt/openiot  
  
# Usuario Administrador Virtuoso  
# Default DBA Virtuoso pass  
ENV VIRTUOSO_DBA_PASS wiser2014  
  
# Geração de chave auto assinada para o JBOSS  
# Configuration of JBOSS self signed SSL KEY  
ENV JBOSS_SSL_KEY "wiser2014"  
ENV JBOSS_SSL_ADDRESS "localhost"  
ENV JBOSS_SSL_ORGANIZATION "WiserUFBA"  
ENV JBOSS_SSL_ORGANIZATION_UNITY "SmartUFBA"  
ENV JBOSS_SSL_CITY "Salvador"  
ENV JBOSS_SSL_STATE "Bahia"  
ENV JBOSS_SSL_COUNTRY "BR"  
# 2 Passo - Instalação dos pré requisitos comuns  
# ---------------------------------------------------------------------------  
# Instalar os prerequisitos globais como alguns ppa e o básico para instalação  
# Step 2 - Pre Installation of requisites for OpenIoT Container  
# ---------------------------------------------------------------------------  
# This step will install base requisites for OpenIoT container, like add the  
# java 8 PPA, maven 3 PPA update the sytem (hmmm this not seeming to be a good
idea)  
# and update sources repo of apt  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
apt-add-repository -y ppa:webupd8team/java && \  
apt-add-repository -y ppa:andrei-pozolotin/maven3 && \  
apt-get update  
  
# 3 Passo - Instalação do Java 7 e Maven  
# ---------------------------------------------------------------------------  
# Instalação do Java 8  
# Step 3 - Java 7 and Maven 3 Installation  
# ---------------------------------------------------------------------------  
# This step will install the latest java 7 and Maven 3  
# Para a Instalação do JAVA 7 é necessário primeiro aceitar a licença do java  
# ---------------------------------------------------------------------------  
# Global accept to oracle license on ubuntu  
RUN echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 " \  
"select true" | /usr/bin/debconf-set-selections  
  
# Agora instalamos o Java 7 e o Maven 3  
# ---------------------------------------------------------------------------  
# Installation of latest oracle java 7 and maven 3  
RUN apt-get install -y oracle-java7-installer && \  
apt-get install -y oracle-java7-set-default && \  
apt-get install -y maven3  
  
# 4 Passo - Instalação do Virtuoso  
# ---------------------------------------------------------------------------  
# Instalação Básica do Virtuoso  
# Step 4 - Virtuoso Installation  
# ---------------------------------------------------------------------------  
# Basic installation of Virtuoso DB  
# Pré requisitos do virtuoso  
# Requisites for Virtuoso DB  
RUN apt-get install -y build-essential debhelper autotools-dev && \  
apt-get install -y autoconf automake unzip wget net-tools && \  
apt-get install -y git libtool flex bison gperf gawk m4 && \  
apt-get install -y libssl-dev libreadline-dev libreadline-dev && \  
apt-get install -y openssl python-pip && \  
pip install crudini  
  
# Virtuoso Release Link Virtuoso 7.2.4.2 (25/04/2016)  
ENV VIRTUOSO_VERSION "7.2.4.2"  
ENV VIRTUOSO_RELEASE_LINK "https://github.com/openlink/virtuoso-
opensource/releases/download/v7.2.4.2/virtuoso-opensource-7.2.4.2.tar.gz"  
# Configuração compilação e instalação do Virtuoso  
# ---------------------------------------------------------------------------  
# This command will install and configure virtuoso, remember that this will
compile  
# virtuoso first  
RUN cd /tmp && \  
mkdir virtuoso_install && \  
cd virtuoso_install && \  
wget -O virtuoso_release.tar.gz $VIRTUOSO_RELEASE_LINK && \  
tar -zxvf virtuoso_release.tar.gz && \  
cd virtuoso-opensource-$VIRTUOSO_VERSION && \  
./autogen.sh && \  
CFLAGS="-O2 -m64" && \  
export CFLAGS && \  
./configure && \  
make && \  
make install && \  
rm -r /tmp/virtuoso_install  
  
# Adiciona o virtuoso  
# Add Virtuoso home to Linux PATH  
ENV PATH $VIRTUOSO_HOME/bin/:$PATH  
  
# Adiciona script de inicialização  
# Add virtuoso service script  
COPY virtuoso-service /etc/init.d/virtuoso-service  
  
# Adiciona o script de inicialização do virtuoso  
# Cria o usuario virtuoso e adiciona as permissões para a DB  
# ---------------------------------------------------------------------------  
# Configure initialization service of Virtuso and added the correct
permissions  
# for properly work.  
RUN chmod 755 /etc/init.d/virtuoso-service && \  
chown root:root /etc/init.d/virtuoso-service && \  
update-rc.d virtuoso-service defaults && \  
printf "RUN=yes\n" > /etc/default/virtuoso && \  
useradd virtuoso --home $VIRTUOSO_HOME && \  
chown -R virtuoso:virtuoso $VIRTUOSO_HOME  
  
# Adiciona a rotina padrão de execução  
# ---------------------------------------------------------------------------  
# Add the standar virtuoso configuration  
COPY virtuoso_config.sh /tmp/virtuoso_config.sh  
  
# Inicializa o serviço do virtuoso, mesmo que ele apresente erros  
# Executa a configuração do virtuoso e remove o arquivo de configuração  
# ---------------------------------------------------------------------------  
# Initialize virtuoso db, check if there no errors and them configure it  
RUN mkdir /usr/local/virtuoso-opensource/var/log && \  
until service virtuoso-service start; do echo "Failed to start... Trying
again."; done && \  
sleep 15 && \  
until bash /tmp/virtuoso_config.sh; do echo "Failed to connect... trying again
in 10 seconds..."; sleep 10; done && \  
rm /tmp/virtuoso_config.sh && \  
service virtuoso-service stop || service virtuoso-service stop  
  
# Expõe as portas do Virtuoso  
# ---------------------------------------------------------------------------  
# Expose Virtuoso Ports  
EXPOSE 8890  
EXPOSE 1111  
# 5 Passo - Instalação do JBOSS  
# ---------------------------------------------------------------------------  
# Instalação do JBOSS  
# Step 5 - JBoss Installation  
# ---------------------------------------------------------------------------  
# JBoss Installation  
# JBOSS Download Link  
ENV JBOSS_DOWNLOAD_LINK "http://download.jboss.org/jbossas/7.1/jboss-
as-7.1.1.Final/jboss-as-7.1.1.Final.zip"  
# Instala os pré-requisitos  
# ---------------------------------------------------------------------------  
# Install the applications needed by JBoss  
RUN apt-get install -y xmlstarlet && \  
apt-get install -y libsaxon-java libsaxonb-java libsaxonhe-java && \  
apt-get install -y libaugeas0 && \  
apt-get install -y unzip bsdtar && \  
# Instala o JBOSS  
mkdir /tmp/jboss_install && \  
cd /tmp/jboss_install && \  
wget -O jboss-install.zip $JBOSS_DOWNLOAD_LINK && \  
unzip jboss-install.zip && \  
mv jboss-as-7.1.1.Final $JBOSS_HOME && \  
rm -r /tmp/jboss_install && \  
mkdir /etc/jboss-as && \  
mkdir /var/log/jboss-as/  
  
# Adiciona o script de inicialização do JBOSS e a configuração  
# ---------------------------------------------------------------------------  
# Add JBoss Service and welcome content  
COPY jboss-service /etc/init.d/jboss-service  
COPY jboss-as.conf /etc/jboss-as/jboss-as.conf  
ADD welcome-content.tar.gz /tmp/  
  
# Adiciona o Jboss a inicialização  
# Cria o usuario jboss e adiciona as permissões para a home do jboss  
# Remove a tela antiga do JBoss  
# ---------------------------------------------------------------------------  
# Add JBoss initialization service in the system  
# Create JBoss user and change permissions of the JBoss home folder  
# And change the correct welcome content  
RUN chmod 755 /etc/init.d/jboss-service && \  
chown root:root /etc/init.d/jboss-service && \  
update-rc.d jboss-service defaults && \  
useradd jboss --home $JBOSS_HOME && \  
chown -R jboss:jboss $JBOSS_HOME && \  
rm -r $JBOSS_HOME/welcome-content && \  
mv /tmp/welcome-content "$JBOSS_HOME/welcome-content"  
  
# Expõe a porta do JBOSS  
# ---------------------------------------------------------------------------  
# Expose JBoss Ports  
EXPOSE 8080  
EXPOSE 8443  
# 6 Passo - Instalação do OpenIot  
# ---------------------------------------------------------------------------  
# Instalação completa do OpenIoT e seus modulos  
# Step 6 - OpenIoT Installation  
# ---------------------------------------------------------------------------  
# Complete installation of OpenIoT and OpenIoT modules  
# JBoss Configuration  
RUN mkdir $JBOSS_HOME/standalone/configuration/ssl && \  
JBOSS_SSL_CONFIG="CN=$JBOSS_SSL_ADDRESS," && \  
JBOSS_SSL_CONFIG="$JBOSS_SSL_CONFIG OU=$JBOSS_SSL_ORGANIZATION_UNITY," && \  
JBOSS_SSL_CONFIG="$JBOSS_SSL_CONFIG O=$JBOSS_SSL_ORGANIZATION," && \  
JBOSS_SSL_CONFIG="$JBOSS_SSL_CONFIG L=$JBOSS_SSL_CITY," && \  
JBOSS_SSL_CONFIG="$JBOSS_SSL_CONFIG S=$JBOSS_SSL_STATE," && \  
JBOSS_SSL_CONFIG="$JBOSS_SSL_CONFIG C=$JBOSS_SSL_COUNTRY" && \  
export JBOSS_SSL_CONFIG && \  
cd $JBOSS_HOME/standalone/configuration/ssl && \  
keytool -genkey \  
-noprompt \  
-alias jbosskey \  
-dname "$JBOSS_SSL_CONFIG" \  
-keyalg RSA \  
-keystore server.keystore \  
-storepass "$JBOSS_SSL_KEY" \  
-keypass "$JBOSS_SSL_KEY" && \  
keytool -export \  
-noprompt \  
-alias jbosskey \  
-file server.crt \  
-keypass "$JBOSS_SSL_KEY" \  
-storepass "$JBOSS_SSL_KEY" \  
-keystore server.keystore && \  
keytool -import \  
-noprompt \  
-alias jbosscert \  
-file server.crt \  
-storepass "$JBOSS_SSL_KEY" \  
-keypass "$JBOSS_SSL_KEY" \  
-keystore server.keystore && \  
keytool -import \  
-noprompt \  
-keystore "$JAVA_HOME/jre/lib/security/cacerts" \  
-file server.crt \  
-alias incommon \  
-storepass changeit && \  
xmlstarlet ed \  
-L \  
-N serverns="urn:jboss:domain:1.2" \  
-N subsystemns="urn:jboss:domain:web:1.1" \  
\--subnode "/serverns:server/_:profile/subsystemns:subsystem" \  
\--type elem \  
-n connector \  
\--insert "//subsystemns:subsystem/connector[not(@name)]" \  
\--type attr \  
-n name \  
-v "https" \  
\--insert "//connector[@name='https']" \  
\--type attr \  
-n protocol \  
-v "HTTP/1.1" \  
\--insert "//connector[@name='https']" \  
\--type attr \  
-n scheme \  
-v "https" \  
\--insert "//connector[@name='https']" \  
\--type attr \  
-n "socket-binding" \  
-v "https" \  
\--insert "//connector[@name='https']" \  
\--type attr \  
-n "secure" \  
-v "true" \  
\--subnode "//connector[@name='https']" \  
\--type elem \  
-n ssl \  
\--insert "//connector[@name='https']/ssl" \  
\--type attr \  
-n name \  
-v "https" \  
\--insert "//ssl" \  
\--type attr \  
-n "key-alias" \  
-v "jbosskey" \  
\--insert "//ssl" \  
\--type attr \  
-n "password" \  
-v "$JBOSS_SSL_KEY" \  
\--insert "//ssl" \  
\--type attr \  
-n "certificate-key-file" \  
-v "$JBOSS_HOME/standalone/configuration/ssl/server.keystore" \  
"$JBOSS_HOME/standalone/configuration/standalone.xml"  
  
# OpenIoT Installation Link  
ENV OPENIOT_LINK https://github.com/OpenIotOrg/openiot.git  
  
# OpenIoT Version  
ENV OPENIOT_BRANCH develop  
# ENV OPENIOT_BRANCH master  
# OpenIoT Compilation  
RUN mkdir /tmp/openiot && \  
cd /tmp/openiot && \  
git clone \--branch $OPENIOT_BRANCH $OPENIOT_LINK && \  
cd /tmp/openiot/openiot && \  
xmlstarlet ed \  
-L \  
-N pomns="http://maven.apache.org/POM/4.0.0" \  
\--subnode "/pomns:project" \  
\--type elem \  
-n repositories \  
\--subnode "/pomns:project/repositories" \  
\--type elem \  
-n repository \  
\--subnode "//repositories/repository" \  
\--type elem \  
-n id \  
-v "wiser-releases" \  
\--subnode "//repository" \  
\--type elem \  
-n url \  
-v "https://github.com/WiserUFBA/wiser-mvn-repo/raw/master/releases" ./pom.xml && \  
export MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=128m" && \  
mvn -X clean install && \  
JBOSS_CONFIGURATION="$JBOSS_HOME/standalone/configuration" && \  
cp ./utils/utils.commons/src/main/resources/security-config.ini
"$JBOSS_CONFIGURATION" && \  
cp ./utils/utils.commons/src/main/resources/properties/openiot.properties
"$JBOSS_CONFIGURATION" && \  
sed --in-place \  
-e "s/scheduler\\.core\\.lsm\\.openiotMetaGraph=.*$/scheduler\\.core\\.lsm\\.openiotMetaGraph=http\:\/\/openiot\\.eu\/OpenIoT\/sensormeta\\#/g" \  
-e "s/scheduler\\.core\\.lsm\\.openiotDataGraph=.*$/scheduler\\.core\\.lsm\\.openiotDataGraph=http\:\/\/openiot\\.eu\/OpenIoT\/sensordata#/g" \  
-e "s/scheduler\\.core\\.lsm\\.openiotFunctionalGraph=.*$/scheduler\\.core\\.lsm\\.openiotFunctionalGraph=http\:\/\/openiot.eu\/OpenIoT\/functionaldata#/g" \  
-e "s/scheduler\\.core\\.lsm\\.sparql\\.endpoint=.*/scheduler\\.core\\.lsm\\.sparql\\.endpoint=http\:\/\/localhost\:8890\/sparql/g" \  
-e "s/scheduler\\.core\\.lsm\\.remote\\.server=.*$/scheduler\\.core\\.lsm\\.remote\\.server=http\:\/\/localhost\:8080\/lsm-light\\.server\//g" \  
-e "s/sdum\\.core\\.lsm\\.openiotFunctionalGraph=.*$/sdum\\.core\\.lsm\\.openiotFunctionalGraph=http\:\/\/openiot\\.eu\/OpenIoT\/functionaldata#/g" \  
-e "s/sdum\\.core\\.lsm\\.sparql\\.endpoint=.*$/sdum\\.core\\.lsm\\.sparql\\.endpoint=http\:\/\/localhost\:8890\/sparql/g" \  
-e "s/sdum\\.core\\.lsm\\.remote\\.server=.*$/sdum\\.core\\.lsm\\.remote\\.server=http\:\/\/localhost\:8080\/lsm-light.server\//g" \  
-e "s/lsm-light\\.server\\.connection\\.url=.*$/lsm-light\\.server\\.connection\\.url=jdbc\:virtuoso\:\/\/localhost\:1111\/log_enable=2/g" \  
-e "s/lsm-light\\.server\\.connection\\.username=.*$/lsm-light\\.server\\.connection\\.username=dba/g" \  
-e "s/lsm-light\\.server\\.connection\\.password=.*$/lsm-light\\.server\\.connection\\.password=$VIRTUOSO_DBA_PASS/g" \  
-e "s/lsm-light\\.server\\.localMetaGraph.*$/lsm-light\\.server\\.localMetaGraph\ =\ http\:\/\/openiot.eu\/OpenIoT\/sensormeta#/g" \  
-e "s/lsm-light\\.server\\.localDataGraph.*$/lsm-light\\.server\\.localDataGraph\ =\ http\:\/\/openiot.eu\/OpenIoT\/sensordata#/g" \  
-e "s/lsm\\.deri\\.ie/localhost\:8080/g" \  
"$JBOSS_CONFIGURATION/openiot.properties" && \  
cd / && \  
mv /tmp/openiot/openiot $OPENIOT_HOME  
  
# Instalação dos Módulos do OpenIoT no Container JBoss  
# ---------------------------------------------------------------------------  
# Configuration and Installation of OpenIoT Modules on JBoss Container  
RUN until service virtuoso-service start; do echo "Failed to start... Trying
again."; done && \  
sleep 30 && \  
until service jboss-service status ; do service jboss-service start; echo
"Started..."; done && \  
sleep 30 && \  
cd "$OPENIOT_HOME/modules/lsm-light/lsm-light.server/" && \  
until mvn -X jboss-as:deploy ; do echo "Failed deploying LSM... trying
again."; done && \  
cd "$OPENIOT_HOME/modules/security/security-server/" && \  
until mvn -X jboss-as:deploy ; do echo "Failed deploying Security Server...
trying again."; done && \  
cd "$OPENIOT_HOME/modules/security/security-management/" && \  
until mvn -X jboss-as:deploy ; do echo "Failed deploying Security
Management... trying again."; done && \  
cd "$OPENIOT_HOME/modules/scheduler/scheduler.core/" && \  
until mvn -X jboss-as:deploy ; do echo "Failed deploying Scheduler Core...
trying again."; done && \  
cd "$OPENIOT_HOME/modules/sdum/sdum.core/" && \  
until mvn -X jboss-as:deploy ; do echo "Failed deploying SDUM Core... trying
again."; done && \  
cd "$OPENIOT_HOME/ui/ui.requestDefinition/" && \  
until mvn -X clean package jboss-as:deploy ; do echo "Failed deploying
requestDefinition... trying again."; done && \  
cd "$OPENIOT_HOME/ui/ui.requestPresentation/" && \  
until mvn -X clean package jboss-as:deploy ; do echo "Failed deploying
requestPresentation... trying again."; done && \  
cd "$OPENIOT_HOME/ui/ui.schemaeditor/" && \  
until mvn -X clean package jboss-as:deploy ; do echo "Failed deploying
schemaeditor... trying again."; done && \  
cd "$OPENIOT_HOME/ui/ide/ide.core/" && \  
until mvn -X clean package jboss-as:deploy ; do echo "Failed deploying IDE
Core... trying again."; done && \  
rm -r /tmp/openiot && \  
service jboss-service stop && \  
( service virtuoso-service stop || service virtuoso-service stop )  
  
# Passo Final  
# ---------------------------------------------------------------------------  
# Ultimas rotinas de compilação da imagem  
# Final Step  
# ---------------------------------------------------------------------------  
# Last routines of image compilation  
# Remove diversas aplicações inúteis  
# TODO: REMOVE ALL UNANTHED APPLICATIONS  
# Finaliza a instalação  
# ---------------------------------------------------------------------------  
# Finished Installation  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history && \  
rm -rf $JBOSS_HOME/standalone/log/* /var/log/* && \  
echo "Finished compilation..."  
  
# Script de inicialização da aplicação  
# ---------------------------------------------------------------------------  
# OpenIoT Start Script  
COPY openiot.sh /openiot.sh  
  
# Ponto de entrada  
# ---------------------------------------------------------------------------  
# Entry point of this appplication  
CMD ["/openiot.sh"]  
  
# References  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/  
# https://github.com/jboss-dockerfiles/base-jdk/blob/jdk7/Dockerfile  
# https://github.com/OpenIotOrg/openiot/wiki/Installation-Guide  
#
https://github.com/OpenIotOrg/openiot/wiki/InstallingVirtuosoOpensource7Ubuntu  
# https://github.com/OpenIotOrg/openiot/wiki/OpenIoT-Virtual-Box-Image---
Documentation  
# https://github.com/OpenIotOrg/openiot/issues/116  
# https://hub.docker.com/_/ubuntu/  
# https://hub.docker.com/r/jboss/base/  
# https://hub.docker.com/r/jboss/base/~/dockerfile/  
# https://hub.docker.com/r/tenforce/virtuoso/~/dockerfile/  
# https://hub.docker.com/r/andreptb/jboss-as/~/dockerfile/  
# http://stackoverflow.com/questions/19335444/how-to-assign-a-port-mapping-to-
an-existing-docker-container  
# http://stackoverflow.com/questions/6880902/start-jboss-7-as-a-service-on-
linux  
# http://stackoverflow.com/questions/15630055/how-to-install-maven-3-on-
ubuntu-15-10-15-04-14-10-14-04-lts-13-10-13-04-12-10-1  
# http://stackoverflow.com/questions/11617210/how-to-properly-import-a-
selfsigned-certificate-into-java-keystore-that-is-avail  
# http://stackoverflow.com/questions/13578134/how-to-automate-keystore-
generation-using-the-java-keystore-tool-w-o-user-inter  
# http://stackoverflow.com/questions/7408545/how-do-you-clear-apache-mavens-
cache  
# https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/  
# http://www.mundodocker.com.br/docker-exec/  
# https://www.digitalocean.com/community/tutorials/docker-explained-using-
dockerfiles-to-automate-building-of-images  
# https://www.technomancy.org/xml/add-a-subnode-command-line-xmlstarlet/  
# http://www.thegeekstuff.com/2009/10/unix-sed-tutorial-how-to-execute-
multiple-sed-commands  
# https://access.redhat.com/documentation/en-
US/JBoss_Enterprise_Application_Platform/6/html/Administration_and_Configuration_Guide/Generate_a_SSL_Encryption_Key_and_Certificate.html  
# https://jbossdivers.wordpress.com/2012/11/20/habilitando-https-no-jboss-
as-7-1-2-jboss-eap-6/  

