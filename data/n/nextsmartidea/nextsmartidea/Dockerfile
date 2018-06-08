FROM node:6.9  
# Create dependencies  
RUN apt-get install -y git  
RUN git clone https://github.com/SebastianBrehme/nextsmartidea  
WORKDIR nextsmartidea/public  
  
# Install app dependencies  
#COPY public/package.json /usr/src/app/  
#RUN npm install -g angular/cli  
#RUN npm install -g firebase-tools  
RUN npm install -g @angular/cli && npm cache clean  
RUN npm install -g firebase-tools  
RUN npm install  
  
# Bundle app source  
EXPOSE 4200  
CMD ng serve --host 0.0.0.0  

