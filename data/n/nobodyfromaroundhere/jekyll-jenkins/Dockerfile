FROM jenkins/jenkins:alpine  
  
# Install Jenkins plugins  
COPY jenkins-plugins.txt /usr/share/jenkins/ref/jenkins-plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/jenkins-
plugins.txt  
  
# Mark Jenkins as configured  
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
-Djenkins.CLI.disabled=true  
# Install Jekyll  
USER root  
  
RUN apk update && apk upgrade  
RUN apk add \--no-cache zlib-dev build-base libxml2-dev libxslt-dev readline-
dev libffi-dev yaml-dev zlib-dev libffi-dev cmake  
RUN apk add \--no-cache ruby ruby-dev ruby-irb ruby-rdoc rsync  
RUN gem update --system && gem install jekyll  
  
# Prep for html-sites volume  
RUN mkdir -p /mnt/html-sites && chown jenkins:jenkins -R /mnt/html-sites  
  
# Update permissions on Ruby gems folder to allow builds to install new
plugins  
RUN chown -R root:jenkins /usr/lib/ruby/gems && chmod 770 -R
/usr/lib/ruby/gems  
  
USER jenkins

