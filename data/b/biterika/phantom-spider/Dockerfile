FROM ubuntu:16.04  
RUN echo '===*********===*********===********* install
===*********===*********===*********'  
  
RUN apt-get update && apt-get install -y --force-yes \  
# python-software-properties \ # mayby not need  
software-properties-common \  
language-pack-en-base \  
curl  
  
#  
#RUN echo '===*********===*********== add-apt-repository ppa:ondrej/php -y
*****===*********===*********'  
#  
#RUN add-apt-repository ppa:ondrej/php -y  
#  
#RUN echo '===*********===*********== apt-get update && apt-get install -y ...
*****===*********===*********'  
#  
#RUN apt-get update && apt-get install -y --force-yes \  
# curl \  
# php7.0-cli \  
# php7.0-curl \  
# php7.0-gd \  
# php7.0-json \  
# imagemagick \  
# git  
RUN echo '===*********===*********== install nodejs6 ...
*****===*********===*********'  
  
#RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
# && apt-get install -y nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
RUN apt-get install -y build-essential  
  
RUN echo "(1)===********* ---->>>>>> check nodejs `node -v | tail -n1`"  
RUN echo "(1)===********* ---->>>>>> check npm `npm -v | tail -n1`"  
  
RUN apt-get update  
  
RUN apt-get install -y libfontconfig  
  
RUN echo '===*********===*********== check nodejs6 ...
*****===*********===*********'  
  
RUN echo "(2)===********* ---->>>>>> check nodejs `node -v | tail -n1`"  
RUN echo "(2)===********* ---->>>>>> check npm `npm -v | tail -n1`"  
  
RUN echo '===*********===*********== prerp proj env...
*****===*********===*********'  
  
RUN mkdir -p /usr/share/biterika/spider  
COPY ./ /usr/share/biterika/spider  
WORKDIR /usr/share/biterika/spider/agent  
ENV appDir /usr/share/biterika/spider/agent  
  
RUN echo '===*********===*********== npm install...
*****===*********===*********'  
  
RUN cd /usr/share/biterika/spider/agent && npm install  
  
RUN echo '===*********===*********== run application...
*****===*********===*********'  
  
ENTRYPOINT ["node", "agent.js", "--no-color", "--no-log"]  
# ENTRYPOINT ["node", "agent.js", "debug"]  
# RUN node run.js 15 --no-color  
# replace this with your application's default port  
EXPOSE 8564

