from jenkins  
  
USER root  
  
RUN mkdir -p /var/lib/jenkins && cd /var/lib/jenkins && curl
https://nodejs.org/dist/v4.2.2/node-v4.2.2-linux-x64.tar.xz | tar x -J  
ENV PATH=/var/lib/jenkins/node-v4.2.2-linux-x64/bin:$PATH  
RUN chown -R jenkins: /var/lib/jenkins/  
  
USER jenkins  
  
COPY plugins.txt /usr/share/jenkins/ref/  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  
COPY create_seed_job.groovy
/usr/share/jenkins/ref/init.groovy.d/create_seed_job.groovy  

