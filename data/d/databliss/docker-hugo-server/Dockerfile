#  
# Runs Hugo static site generator as a local server  
#  
FROM databliss/docker-hugo:latest  
MAINTAINER Randolph Kahle "randolph.kahle@databliss.net"  
  
WORKDIR /site  
ENV VIRTUAL_HOST="http://docker.local:1313"  
  
EXPOSE 1313  
  
CMD hugo server \--renderToDisk --watch \--bind="0.0.0.0"
\--baseURL="${VIRTUAL_HOST}" \--navigateToChanged /site  

