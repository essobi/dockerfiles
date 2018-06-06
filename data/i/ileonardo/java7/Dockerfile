# x) - docker build -t ileonardo/java7 .  
# y) - Às Instruções fica nas Dependências e no final do arquivo: [REGRA] # z)  
### Base da Imagem  
FROM ileonardo/base-ubuntu  
  
### Autor  
MAINTAINER iLeonardo Carvalho <i.leonardo.c.c@outlook.com>  
  
### Dependências  
ENV JAVA="7"  
  
ENV JAVA_HOME="/usr/lib/jvm/java-${JAVA}-oracle" \  
PATH="$PATH:${JAVA_HOME}/bin"  
### Start  
# Usando a base do Container Original.  
# ----------  
# NO PORTS  
# CMD bash  
### Pacotes Essenciais  
RUN echo oracle-java${JAVA}-installer shared/accepted-oracle-license-v1-1
select true | debconf-set-selections; \  
{ \  
echo '# Java'; \  
echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main'; \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main ';
\  
} >> /etc/apt/sources.list; \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
7B2C3B0889BF5709A105D03AC2518248EEA14886; \  
apt-get update; apt-get --no-install-recommends -qqy install \  
oracle-java${JAVA}-installer \  
ca-certificates; \  
# Configurando o JAVA  
chmod -R 755 ${JAVA_HOME}; \  
echo "JAVA_HOME=${JAVA_HOME}" >> /etc/environment; \  
sed -i '/PATH/c\PATH='"'$PATH:${JAVA_HOME}/bin\'"'' /etc/environment; \  
### Limpando os Pacotes desnecessários  
apt-get -qqy autoremove; \  
apt-get autoclean; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /var/cache/oracle-jdk${JAVA}-installer \  
${JAVA_HOME}/R* \  
${JAVA_HOME}/LICENSE \  
${JAVA_HOME}/src.zip \  
${JAVA_HOME}/THI*  
  
# z) docker run -dit ileonardo/java7  

