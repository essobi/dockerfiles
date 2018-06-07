FROM jenkins:latest  
MAINTAINER Vedran Lerenc <vlerenc@gmail.com>  
  
# Add entrypoint/command scripts  
ADD scripts /scripts  
# ..ugly workaround as Jenkins is not the owner (see
https://github.com/docker/docker/issues/6119)  
USER root  
RUN chown -R jenkins:jenkins /scripts  
USER jenkins  
# ..ugly workaround end (see above)  
RUN chmod +x /scripts/*.sh  
  
# Force initialization on first container run  
RUN touch /scripts/.first_run  
  
# Entrypoint/command to run (overwriting parent)  
ENTRYPOINT ["/scripts/run.sh"]  
CMD [""]  
  
# Listening ports defined in parent  
# 8080 for web interface and 50000 for slaves  
# Data volumes defined in parent  
# /var/jenkins_home for all data, jobs, plugins, etc.  

