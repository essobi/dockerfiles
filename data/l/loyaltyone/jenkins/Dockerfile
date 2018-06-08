FROM jenkins/jenkins:2.103  
  
COPY entry-point /usr/local/bin/  
  
USER root  
RUN apt-get update && apt-get install -y gosu python-pip  
RUN pip install awscli  
  
ENTRYPOINT ["/usr/local/bin/entry-point", "/sbin/tini", "--",
"/usr/local/bin/jenkins.sh"]

