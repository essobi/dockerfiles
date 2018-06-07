FROM java:8-jdk  
  
MAINTAINER Elementar Sistemas <contato@elementarsistemas.com.br>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# instala os pacotes necessários do SO  
RUN apt-get update \  
&& apt-get install -y curl unzip sudo make ruby \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# instala a gema rake  
RUN gem install rake  
  
# instala o docker  
ENV DOCKER_VERSION="1.12.1"  
RUN curl -sL "https://get.docker.com/builds/Linux/`uname
-m`/docker-${DOCKER_VERSION}.tgz" \  
| tar xvz --strip-components 1 -C /usr/local/bin/ \  
&& docker --version  
  
# instala o docker-compose  
ENV DOCKER_COMPOSE_VERSION="1.8.0"  
RUN curl -sL
"https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m`" \  
> /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& docker-compose --version  
  
# define as variáveis básicas de ambiente  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
# copia o script de configuração do agente  
RUN echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/teamcity  
ADD setup-agent.sh entrypoint.sh /usr/local/bin/  
  
# expoe a porta 9090  
EXPOSE 9090  
# cria usuário para o TeamCity  
RUN useradd -u 1000 -Urm teamcity -G sudo  
  
# define o comando padrão para rodar o agente  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["setup-agent.sh"]  

