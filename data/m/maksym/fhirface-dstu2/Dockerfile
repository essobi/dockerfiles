FROM ubuntu:14.10  
MAINTAINER Maksym Bodnarchuk <bodnarchuk@gmail.com>  
  
ENV REFRESHED_AT 2015-03-04  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y curl git  
  
USER root  
  
RUN useradd --user-group --create-home --shell /bin/bash fhir && echo
'fhir:fhir' | chpasswd && adduser fhir sudo  
RUN echo 'fhir ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
USER fhir  
  
ENV HOME /home/fhir  
ENV PATH /home/fhir/bin:$PATH  
ENV NVM_DIR /home/fhir/.nvm  
  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.23.3/install.sh |
bash  
RUN . ~/.nvm/nvm.sh && nvm install 0  
  
ADD . /home/fhir/fhirface  
WORKDIR /home/fhir/fhirface  
RUN sudo chown fhir:fhir -R ./  
RUN git submodule init && git submodule update  
RUN . ~/.nvm/nvm.sh && nvm use 0 && npm install && `npm bin`/bower install  
  
EXPOSE 6000  
ENV PORT 6000  
ENV BASEURL http://fhirplace.coreos.health-samurai.io:10001  
CMD . ~/.nvm/nvm.sh && nvm use 0 && npm start  

