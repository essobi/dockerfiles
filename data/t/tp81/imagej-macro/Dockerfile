FROM fiji/fiji:latest  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y xvfb  
RUN sudo cp jars/ij-*.jar ij.jar  
RUN echo "xvfb-run java -jar ij.jar -batch \$*" >go.sh  
  
ENTRYPOINT ["sh","go.sh"]  

