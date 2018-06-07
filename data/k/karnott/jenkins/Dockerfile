FROM jenkins/jenkins:lts  
  
USER root  
RUN echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update  
RUN apt-get install -y apt-utils nodejs build-essential yarn && wget
https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/4.1.2/flyway-
commandline-4.1.2-linux-x64.tar.gz && tar -xvf flyway-
commandline-4.1.2-linux-x64.tar.gz && rm flyway-
commandline-4.1.2-linux-x64.tar.gz  
  
# INSTALL DOCKER  
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg2
software-properties-common  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(.
/etc/os-release; echo "$ID") $(lsb_release -cs) stable"  
RUN apt-get update  
RUN apt-get install -y docker-ce  
# INSTALL DOCKER-COMPOSE  
RUN curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
# Install Az  
RUN apt-get update  
RUN apt-get install -y python libssl-dev libffi-dev python-dev build-essential  
COPY resources/azure-cli-script /tmp/azure-cli-script  
RUN chmod +x /tmp/azure-cli-script  
RUN /tmp/azure-cli-script  
  
# Install Flyway  
RUN mkdir /flyway  
RUN curl "https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/4.2.0/flyway-commandline-4.2.0-linux-x64.tar.gz" >
/flyway/install.tar.gz  
RUN cd /flyway && tar zxfv install.tar.gz  
RUN chmod 755 /flyway/flyway-4.2.0/flyway  
RUN ln -s /flyway/flyway-4.2.0/flyway /bin/flyway  
  
# Install Asciidoctor  
RUN apt-get install -y asciidoctor && gem install --no-document rake rouge
coderay thread_safe slim haml tilt  
  
USER jenkins  

