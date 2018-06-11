# use the ubuntu base image  
FROM ubuntu  
  
MAINTAINER Urban Faubion <urban.faubion@gmail.com>  
  
# INSTALL NODE  
# ------------  
# get node deps  
RUN apt-get update  
RUN apt-get install -y build-essential python wget  
  
# get node v0.10.26  
RUN wget http://nodejs.org/dist/v0.10.26/node-v0.10.26.tar.gz  
RUN tar -zxvf node-v0.10.26.tar.gz  
RUN rm node-v0.10.26.tar.gz  
WORKDIR node-v0.10.26  
  
# install node  
RUN ./configure  
RUN make  
RUN make install  
  
# cleanup node  
WORKDIR ..  
RUN rm -r node-v0.10.26  
RUN apt-get remove -y build-essential python wget  
  
# install git  
RUN apt-get install -y git  
RUN git config --global url."https://".insteadOf git://  
  
# install app  
ONBUILD ADD ./app /opt/app  
ONBUILD WORKDIR /opt/app  
ONBUILD RUN npm install  
  
# expose container  
EXPOSE 80  
# start  
CMD ["npm", "start"]

