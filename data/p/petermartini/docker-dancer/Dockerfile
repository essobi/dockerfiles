FROM perl:5.20.0  
MAINTAINER Peter Martini <PeterCMartini@GMail.com>  
  
WORKDIR /root  
  
# YAML is a "soft" dependency, but its apparently needed for even the default
CMD below  
RUN cpanm YAML  
  
# Install Dancer itself  
RUN cpanm Dancer  
  
EXPOSE 3000  
# If no arguments passed, create a HelloWorld  
CMD dancer -a Hello::World; cd Hello-World; ./bin/app.pl  

