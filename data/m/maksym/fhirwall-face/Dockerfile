FROM ubuntu:14.10  
MAINTAINER Danil Kutkevich <danil@kutkevich.org>, Maksym Bodnarchuk
<bodnarchuk@gmail.com>  
  
ENV REFRESHED_AT 2015-02-19  
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
RUN bash -lc 'source ~/.nvm/nvm.sh && nvm install 0'  
  
ADD . /home/fhir/fhirwall-face  
WORKDIR /home/fhir/fhirwall-face  
RUN sudo chown fhir:fhir -R ./  
RUN . ~/.nvm/nvm.sh && nvm use 0 && npm install && `npm bin`/bower install  
  
EXPOSE 6001  
ENV PORT 6001  
ENV FHIRWALL_URI http://localhost:6000  
ENV FHIRWALL_PATH /oauth  
  
CMD . ~/.nvm/nvm.sh && nvm use 0 && npm start  

