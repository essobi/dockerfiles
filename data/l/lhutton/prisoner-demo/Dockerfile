# Dockerfile for PRISONER Demonstration  
# http://prisoner.cs.st-andrews.ac.uk  
# Version 0.1.1  
# Last updated June 20th 2016  
FROM lhutton/prisoner  
MAINTAINER Luke Hutton <luke.hutton@open.ac.uk>  
LABEL Description="This image prepares an environment for a trivial
demonstration of PRISONER."  
  
COPY ./ /usr/bin/prisoner-demo  
  
EXPOSE 9000  
CMD ["bin/bash","/usr/bin/prisoner-demo/start_demo.sh"]  

