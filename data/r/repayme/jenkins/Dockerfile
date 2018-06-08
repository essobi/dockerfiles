FROM jenkinsci/jenkins  
MAINTAINER Oliver Schwab  
  
# install plugins  
RUN /usr/local/bin/install-plugins.sh git  
RUN /usr/local/bin/install-plugins.sh github  
RUN /usr/local/bin/install-plugins.sh gradle  
RUN /usr/local/bin/install-plugins.sh workflow-aggregator  
RUN /usr/local/bin/install-plugins.sh email-ext  
RUN /usr/local/bin/install-plugins.sh all-changes  
  
# skip setup wizard  
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false"  
# execute the following with root permissions  
USER root  
  
# download maven and git  
RUN apt-get update --fix-missing  
RUN apt-get install -y \  
maven \  
git  
  
# copy init script and give permission  
COPY init.sh /  
RUN chmod +x /init.sh  
  
# download and extract docker binaries (latest)  
RUN wget http://get.docker.com/builds/Linux/x86_64/docker-latest.tgz  
RUN tar -xvzf /docker-latest.tgz \  
&& mv docker/* /usr/bin/  
  
# download and install docker-compose (v 1.10.0)  
RUN curl -L https://github.com/docker/compose/releases/download/1.10.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
# grant permission to parent docker  
RUN groupadd -g 999 docker \  
&& gpasswd -a jenkins docker  
  
# drop back to regular jenkins user  
USER jenkins  
  
# start custom init script  
ENTRYPOINT ["/bin/tini", "--", "/init.sh"]  

