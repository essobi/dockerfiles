FROM debian  
  
RUN apt-get update --yes  
RUN apt-get upgrade --yes  
  
RUN apt-get install --yes curl gnupg cron git  
RUN sed -i '/session required pam_loginuid.so/c\\#session required
pam_loginuid.so' /etc/pam.d/cron  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install --yes nodejs  
  
RUN useradd http  
RUN mkdir /home/http && chown http:http /home/http  
  
# fetch the server and install dependencies  
RUN su - http -c "git clone https://github.com/k13-engineering/webpage-
server.git; cd webpage-server; npm install"  
# fetch the content  
RUN su - http -c "git clone https://github.com/k13-engineering/webpage-
content.git"  
  
COPY pull-webpage-content.cron /etc/cron.d/pull-webpage-content  
COPY init.sh /home/http  
  
ENV NODE_ENV=production  
WORKDIR /home/http  
CMD [ "./init.sh" ]  

