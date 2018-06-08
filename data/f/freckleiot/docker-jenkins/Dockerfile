FROM jenkins/jenkins:2.118  
  
COPY entry-point /usr/local/bin/  
  
# Become the root user and install gosu and AWS CLI  
USER root  
RUN apt-get update && apt-get install -y gosu python-pip rsync jq  
RUN pip install awscli  
  
# Execute the entry-point which adds the user with the correct permissions
needed to interact with the volume mount  
# After the entry-point, we drop from the `root` user to the `user` user which
has the correct permissions  
ENTRYPOINT ["/usr/local/bin/entry-point", "/sbin/tini", "--",
"/usr/local/bin/jenkins.sh"]  

