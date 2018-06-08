FROM java:8  
ADD http://mirrors.muzzy.org.uk/apache/nutch/1.10/apache-nutch-1.10-bin.zip
/apache-nutch.zip  
RUN apt-get install -y unzip  
RUN unzip /apache-nutch.zip  
RUN mv /apache-nutch-1.10 /nutch  
RUN rm /apache-nutch.zip  
  
WORKDIR /nutch  

