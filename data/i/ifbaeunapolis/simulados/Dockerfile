FROM jenkins:latest  
  
# Modificando o número de executores  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
  
# Todos os comandos a partir desse serão executados no usuário root  
USER root  
  
# Instalando dependências do latex e auto-multiple-choice  
RUN sed -i 's;http://httpredir.debian.org;http://ftp.br.debian.org;'
/etc/apt/sources.list  
RUN apt-get clean  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
texlive-luatex \  
auto-multiple-choice \  
texlive-latex-extra \  
texlive-lang-portuguese \  
texlive-fonts-recommended \  
lua-filesystem \  
xlsx2csv \  
lmodern  
  
RUN apt-get autoremove -y  
RUN apt-get clean  
  
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
  
# Instalando Plugins do Jenkins  
RUN /usr/local/bin/install-plugins.sh \  
script-security:1.13 \  
envinject:1.92.1 \  
build-pipeline-plugin:1.5.3.1 \  
email-ext:2.44 \  
git:2.5.2 \  
copyartifact:1.38.1  
  
# Criar pasta de usuário do jenkins  
RUN mkdir /home/jenkins  
RUN chown jenkins:jenkins /home/jenkins  
  
# Retornar ao usuário do jenkins  
RUN chown -R jenkins /var/jenkins_home /usr/share/jenkins/ref  
COPY config.xml /usr/share/jenkins/ref/config.xml  
COPY jobs/ /usr/share/jenkins/ref/jobs  
  
USER jenkins  

