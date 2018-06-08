FROM ubuntu:trusty  
  
MAINTAINER tony.hirst@gmail.com  
  
# Install Headless JRE after updating installed packages.  
RUN apt-get update && apt-get install -y wget ant unzip openjdk-7-jdk && apt-
get clean  
  
#Build OpenRefine  
RUN wget --no-check-certificate
https://github.com/OpenRefine/OpenRefine/archive/master.zip  
RUN unzip master.zip && rm master.zip  
  
RUN OpenRefine-master/refine build  
  
#Tidy up  
RUN apt-get remove -y openjdk-7-jdk  
  
#RUN wget --no-check-certificate
https://github.com/OpenRefine/OpenRefine/releases/download/2.6-beta.1/openrefine-
linux-2.6-beta.1.tar.gz  
#RUN tar -xzf openrefine-linux-2.6-beta.1.tar.gz && rm openrefine-
linux-2.6-beta.1.tar.gz  
RUN apt-get install openjdk-7-jre-headless  
  
EXPOSE 3333  
RUN mkdir /mnt/refine  
#CMD ["openrefine-2.6-beta.1/refine", "-i", "0.0.0.0", "-d", "/mnt/refine"]  
CMD ["OpenRefine-master/refine", "-i", "0.0.0.0", "-d", "/mnt/refine"]

