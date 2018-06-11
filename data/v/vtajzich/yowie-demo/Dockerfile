FROM vtajzich/java:oracle-java8  
MAINTAINER Vitek Tajzich <v.tajzich@vendavo.com>  
RUN mkdir /home/app  
ADD https://github.com/vtajzich/yowie-demo/releases/download/1.0.0/movie-
finder.tar /home/app/  
  
WORKDIR /home/app  
  
RUN tar -xvf /home/app/movie-finder.tar && rm /home/app/movie-finder.tar  
  
EXPOSE 8080  
CMD /home/app/movie-finder/bin/movie-finder  

