FROM masashikurita/docker-jenkins-job-builder  
MAINTAINER Masashi Kurita <marty.marron@gmail.com>  
  
USER jenkins_jobs  
WORKDIR /home/jenkins_jobs  
COPY config.sh ./  
RUN mkdir jobs  
COPY jobs ./jobs/  
  
ENTRYPOINT ["/home/jenkins_jobs/config.sh"]

