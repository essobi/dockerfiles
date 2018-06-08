FROM perl:latest  
MAINTAINER Nick Langridge  
  
RUN curl -L http://cpanmin.us | perl - App::cpanminus  
RUN git clone https://github.com/nicklangridge/docker-test.git  
RUN cd docker-test && cpanm --installdeps .  
  
EXPOSE 3000  
WORKDIR docker-test  
CMD morbo server.pl  

