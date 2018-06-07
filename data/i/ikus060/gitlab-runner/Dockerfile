FROM gitlab/gitlab-runner  
MAINTAINER Patrik Dufresne <info@patrikdufresne.com>  
  
ADD runner.sh /runner.sh  
RUN chmod +x /runner.sh  
  
ENTRYPOINT ["/runner.sh"]  

