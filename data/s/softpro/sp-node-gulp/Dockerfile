FROM node  
  
# add a normal default jenkins user  
#RUN useradd -ms /bin/bash jenkins  
#USER jenkins  
#ENV HOME /home/jenkins  
#WORKDIR /home/jenkins  
RUN mkdir -p /data  
WORKDIR /data  
  
RUN npm install -g gulp  
#RUN npm install phantomjs2  
#ENV PHANTOMJS_BIN=/data/node_modules/phantomjs2/lib/phantom/bin/phantomjs  
#ENV PATH=$PATH:/data/node_modules/phantomjs2/lib/phantom/bin  
ONBUILD COPY package.json /data/  
ONBUILD COPY .npmrc /data/  
ONBUILD COPY gulpfile.js /data/  
ONBUILD RUN npm install  
ONBUILD COPY . /data/  
  
# Define default command.  
CMD ["/bin/bash", "-c"]  

