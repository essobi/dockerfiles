#Second Dockerfile  
FROM ubuntu  
MAINTAINER Dan Powers <dan.powers@docker.com>  
ADD . /opt  
RUN apt-get update  
RUN apt-get install -y g++  
RUN g++ -o /opt/Grades.exe /opt/Grades.cpp  
CMD ["/opt/Grades.exe"]  
  

