FROM tedneward/openjdk8  
MAINTAINER Ted Neward (ted@tedneward.com)  
  
# May seem weird that openjdk9src depends on openjdk8; this is  
# because the build for OpenJDK9 depends on a OpenJDK8 boot JDK  
VOLUME ["/home"]  
  
COPY getSource.sh /usr/local/bin  
COPY configure.sh /usr/local/bin  
COPY deployBuild.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/*.sh  
  
ENV PATH /opt/openjdk9/bin:${PATH}  
ENV JAVA_HOME /opt/openjdk9  
  
CMD ["/bin/bash"]  

