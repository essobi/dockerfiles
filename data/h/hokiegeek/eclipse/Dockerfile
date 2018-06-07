FROM openjdk:8  
RUN mkdir /workspace  
VOLUME /workspace  
  
RUN wget --output-document /tmp/eclipse-java.tar.gz
'https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/neon/R/eclipse-
java-neon-R-linux-gtk-x86_64.tar.gz&r=1'  
  
# COPY eclipse-java-neon-R-linux-gtk-x86_64.tar.gz /tmp/eclipse-java.tar.gz  
RUN cd /opt && tar -xvzf /tmp/eclipse-java.tar.gz && rm -rf /tmp/eclipse-
java.tar.gz  
  
WORKDIR /workspace  
  
CMD ["/opt/eclipse/eclipse"]  

