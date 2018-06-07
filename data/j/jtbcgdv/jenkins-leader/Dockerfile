FROM jenkins:latest  
  
MAINTAINER James Thimont <james.thimont@bcgdv.com>  
  
# Install plugins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
# Copy Jenkins config  
USER root  
COPY jenkins /usr/share/jenkins/ref  
RUN chown -R jenkins:jenkins /usr/share/jenkins/ref  
  
USER root  
  
RUN apt-get update && apt-get install -y -qq --no-install-recommends wget
unzip python openssh-client rsync python-pip \  
&& apt-get clean  
  
RUN pip install awscli  
  
USER jenkins  
COPY start.sh /usr/local/bin/start.sh  
  
VOLUME /usr/jenkins  
  
ENTRYPOINT ["/usr/local/bin/start.sh"]

