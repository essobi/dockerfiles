FROM docker.bintray.io/jfrog/artifactory-pro:5.8.3  
MAINTAINER Philipp Goellner <philipp.goellner@xaltbc.de>  
  
ENV ARTIFACTORY_HOME /opt/jfrog/artifactory  
  
ENV TIME_ZONE false  
  
ENV BACKUP_HOST false  
ENV BACKUP_PATH false  
ENV BACKUP_USER false  
ENV BACKUP_KEY_FILE /tmp/id_rsa  
  
USER root  
  
COPY configure-and-start-root.sh /  
RUN chmod u+x /configure-and-start-root.sh \  
&& apt-get update --quiet \  
&& apt-get install --quiet -y --no-install-recommends openssh-client \  
rsync \  
&& apt-get clean  
  
VOLUME ["${ARTIFACTORY_HOME}"]  
  
ENTRYPOINT ["/configure-and-start-root.sh"]  

