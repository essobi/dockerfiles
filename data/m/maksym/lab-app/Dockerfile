FROM ubuntu:14.10  
MAINTAINER Maksym Bodnarchuk <bodnarchuk@gmail.com>  
  
ENV REFRESHED_AT 2015-03-03  
RUN apt-get -y update  
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
  
ADD . /home/fhir/lab-app  
WORKDIR /home/fhir/lab-app  
RUN sudo chown fhir:fhir -R ./  
RUN . ~/.nvm/nvm.sh && nvm use 0 && npm install && `npm bin`/bower install  
  
EXPOSE 6002  
ENV PORT 6002  
ENV BASEURL http://localhost:6000/fhir  
ENV OAUTH_CLIENT_ID lab-app-client-id  
ENV OAUTH_CLIENT_SECRET lab-app-client-secret  
ENV OAUTH_REDIRECT_URI http://localhost:6002/#/redirect  
ENV OAUTH_SCOPE user  
ENV OAUTH_RESPONSE_TYPE token  
ENV OAUTH_AUTHORIZE_URI http://localhost:6000/oauth/authorize  
  
CMD . ~/.nvm/nvm.sh && nvm use 0 && npm start  

