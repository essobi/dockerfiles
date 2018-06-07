FROM kalilinux/kali-linux-docker:latest  
  
RUN apt-get update && apt-get clean all  
RUN apt-get upgrade -y && apt-get clean all  
RUN apt-get install kali-linux -y && apt-get clean all  
  
CMD ["/bin/bash"]  

