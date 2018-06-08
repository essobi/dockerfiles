FROM josteinaj/daisy-pipeline  
  
MAINTAINER Jostein Austvik Jacobsen  
  
WORKDIR /home/root/  
  
# Install Nordic EPUB3/DTBook Migrator  
ADD dependencies /home/root/dependencies/  
RUN mv /home/root/dependencies/* /home/root/daisy-pipeline/modules/  
RUN wget
https://oss.sonatype.org/content/repositories/releases/org/daisy/pipeline/modules/nordic-
epub3-dtbook-migrator/1.0.0/nordic-epub3-dtbook-migrator-1.0.0.jar && mv *.jar
/home/root/daisy-pipeline/modules/  
  
#CMD ["/home/root/daisy-pipeline/cli/dp2", "help"]  

