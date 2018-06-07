FROM node  
  
#Specifies the directory we'll be working with  
WORKDIR /src  
  
#ADD and COPY are similar, but COPY is preferred due to more transparency  
#Tip: avoid using add to fetch packages, use curl/wget  
COPY package.json /src/package.json  
  
#Installs dependencies  
RUN npm install  
  
#Bundles app source  
#For production level docker files, check out 'Docker Cache' for better
efficiency  
COPY . /src/  
  
#Makes the port available  
EXPOSE 3000  
CMD ["node", "/src/app.js"]  

