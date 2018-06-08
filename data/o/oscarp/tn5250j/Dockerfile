#  
# TN5250J Dockerfile  
#  
# Terminal Emulator  
#  
# Pull base image.  
FROM ubuntu:latest  
  
# Install.  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y default-jre  
RUN apt-get install -y wget unzip  
RUN cd /tmp ; wget
http://sourceforge.net/projects/tn5250j/files/tn5250j/0.7.5/tn5250j-0.7.5-full-
bin.zip  
RUN cd /tmp && unzip tn5250j-0.7.5-full-bin.zip -d tn5250  
RUN cd /tmp/tn5250 && mv tn5250j-0.7.5 /usr/local/tn5250j  
RUN rm -rf /var/lib/apt/lists/*  
  
# Define default command.  
CMD ["/usr/bin/java","-jar","/usr/local/tn5250j/tn5250j.jar"]  

