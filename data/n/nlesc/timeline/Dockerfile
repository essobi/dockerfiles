FROM node:4  
RUN mkdir /timeline  
COPY ./ /timeline/  
EXPOSE 9000  
WORKDIR /timeline  
RUN npm install  
RUN npm rebuild node-sass  
RUN npm install -g bower gulp  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN bower install  
RUN gulp build  
CMD gulp serve  

