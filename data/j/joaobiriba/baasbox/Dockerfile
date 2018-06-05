FROM dockerfile/java  
MAINTAINER Giovanni Laquidara <glaquidara@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y && \  
apt-get install software-properties-common -y && \  
apt-get install -y wget && \  
apt-get install -y unzip  
RUN wget http://www.baasbox.com/download/baasbox-stable.zip  
RUN unzip -o baasbox-stable.zip  
RUN chmod 755 baasbox-0.8.3/start  
  
EXPOSE 9000  
CMD baasbox-0.8.3/start  

