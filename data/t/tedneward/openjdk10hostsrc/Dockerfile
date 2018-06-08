FROM tedneward/openjdk9  
MAINTAINER Ted Neward (ted@tedneward.com)  
  
# May seem weird that openjdk10src depends on openjdk9; this is  
# because the build for OpenJDK10 depends on a OpenJDK9 boot JDK  
VOLUME ["/home"]  
  
COPY getSource.sh /home  
COPY configure.sh /home  
COPY deployBuild.sh /home  
RUN cd home && chmod +x *.sh  
  
CMD ["/bin/bash"]  

