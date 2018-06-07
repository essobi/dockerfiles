FROM tifayuki/java:java8  
  
RUN apt-get update -y  
RUN apt-get install -y x11-utils git-core  
  
RUN wget http://download.jetbrains.com/idea/ideaIC-13.1.3.tar.gz  
RUN mkdir /opt/intelij  
RUN tar -xf ideaIC-13.1.3.tar.gz -C /opt/intelij  
RUN rm ideaIC-13.1.3.tar.gz  
ADD idea64.vmoptions /opt/intelij/idea-IC-135.909/bin/idea64.vmoptions  
ADD idea.properties /opt/intelij/idea-IC-135.909/bin/idea.properties  
  
VOLUME /data  
  
CMD /opt/intelij/idea-IC-135.909/bin/idea.sh  

