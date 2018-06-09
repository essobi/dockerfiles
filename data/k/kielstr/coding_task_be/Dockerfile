  
FROM perl:latest  
MAINTAINER Kiel R Stirling kielstr@cpan.org  
  
RUN curl -L http://cpanmin.us | perl - App::cpanminus  
RUN cpanm Dancer2 Starman  
RUN apt-get update && apt-get -y install wamerican  
  
ARG CACHE_DATE=2016-01-02  
RUN git clone https://github.com/kielstr/Coding-task-BE.git  
  
EXPOSE 80  
WORKDIR Coding-task-BE  
#CMD plackup -R lib -r --port 8080 bin/app.psgi  
CMD plackup -s Starman --workers=10 -p 80 -a bin/app.psgi  
  

