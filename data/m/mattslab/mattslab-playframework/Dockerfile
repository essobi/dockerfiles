FROM ingensi/oracle-jdk  
MAINTAINER Matthew Browning <MC.FallenYouth@gmail.com>  
  
RUN yum install -y unzip  
  
EXPOSE 9000  
RUN mkdir /app  
WORKDIR /app  
  
CMD ["activator" "run"]

