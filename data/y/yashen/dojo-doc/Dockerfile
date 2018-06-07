FROM ubuntu:15.10  
MAINTAINER yashen@gmail.com  
  
RUN apt-get update  
RUN apt-get install nodejs -y  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install vim -y  
RUN apt-get install npm -y  
RUN npm update  
RUN npm install express  
RUN npm install jade  
RUN apt-get install python2.7 -y  
RUN apt-get install python-pip -y  
RUN apt-get install default-jre -y  
RUN apt-get install git -y  
RUN pip install cheetah cherrypy docutils pygments  
RUN apt-get install Make -y  
RUN apt-get install supervisor -y  
  
RUN mkdir /dojo  
WORKDIR /dojo  
RUN git clone https://github.com/dojo/dojo.git  
RUN git clone https://github.com/dojo/dijit.git  
RUN git clone https://github.com/dojo/dojox.git  
RUN git clone https://github.com/dojo/util.git  
RUN git clone https://github.com/dojo/demos.git  
RUN git clone https://github.com/dojo/docs.git  
RUN git clone \--recursive https://github.com/lbod/dapi.git  
RUN git clone \--recursive https://github.com/wkeese/js-doc-parse.git  
RUN git clone https://github.com/phiggins42/rstwiki.git  
  
ADD Makefile Makefile  
RUN make rstwiki_build  
EXPOSE 4200  
EXPOSE 8000  
ADD dapi_config dapi_config  
ADD Makefile Makefile  
RUN make doc1.9  
RUN make doc1.10  
EXPOSE 3000  
RUN make dapilib  
ADD dapi_config/dapiconfig.js dapi/config.js  
RUN cd dapi;npm update  
  
ADD Makefile Makefile  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf && /bin/bash  

