FROM jenkins/jenkins:lts  
  
# if we want to install via apt  
USER root  
  
# Base stuff required  
RUN apt-get update \  
&& apt-get install curl gnupg apt-transport-https  
  
# PowerShell UBU  
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
# && curl -o /etc/apt/sources.list.d/microsoft.list
https://packages.microsoft.com/config/ubuntu/16.04/prod.list \  
# && apt-get update \  
# && apt-get install -y powershell  
# Powershell Stretch  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch
main" > /etc/apt/sources.list.d/microsoft.list' \  
&& apt-get update \  
&& apt-get install -y powershell  
  
RUN mkdir -p /var/jenkins_plugins && chown jenkins:jenkins
/var/jenkins_plugins  
  
USER jenkins  
  
# Plugins  
# TODO: Clean out this plugins list, to just the bare minimum needed  
COPY config/plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
# Overwrite jenkins setup script with our custom one  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  
# Hook scripts  
COPY config/init.groovy.d/*.groovy /usr/share/jenkins/ref/init.groovy.d/  
COPY config/boot-failure.groovy.d/*.groovy /usr/share/jenkins/ref/boot-
failure.groovy.d/  
COPY bootstrap/*.sh /usr/share/jenkins/ref/bootstrap/  
  
# Just in case the scripts aren't exec  
USER root  
RUN chmod a+x /usr/local/bin/jenkins.sh  
RUN chmod a+x /usr/share/jenkins/ref/bootstrap/*.sh  
RUN chown 1000:1000 /usr/share/jenkins/ref/bootstrap/*.sh  
  
# Ensure base dirs created as jenkins, so we can mount if needed  
RUN mkdir -p /usr/share/jenkins/ref/secrets && mkdir -p
/usr/share/jenkins/ref/plugins && mkdir -p /usr/share/jenkins/ref/jobs &&
mkdir -p /usr/share/jenkins/ref/nodes  
RUN touch /usr/share/jenkins/ref/secrets/.placehold.me && touch
/usr/share/jenkins/ref/plugins/.placehold.me && touch
/usr/share/jenkins/ref/jobs/.placehold.me && touch
/usr/share/jenkins/ref/nodes/.placehold.me  
  
# Minio is handy for copying over template files  
RUN curl -L https://dl.minio.io/client/mc/release/linux-amd64/mc >
/usr/local/bin/mc && \  
chmod +x /usr/local/bin/mc  
  
# Let's copy everything as a template  
RUN mkdir -p /var/jenkins_template && chown jenkins:jenkins
/var/jenkins_template  
RUN cp -R /var/jenkins_home/* /var/jenkins_template  
  
USER jenkins  
  
# TODO: Use Jenkins CAAS project  
# TODO: Script to run and Copy bootstrap files?  
# For now, rely on /usr/share/jenkins/ref/  

