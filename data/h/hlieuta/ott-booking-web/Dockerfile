FROM node:slim  
  
# Install app dependencies  
COPY package.json /src/package.json  
RUN cd /src; npm install  
  
# Bundle app source  
COPY . /src  
  
ENV NODE_ENV=production  
ENV APP_NAME="OTT Booking"  
ENV RESET_PASSWORD_EMAIL="OTT<no-reply@ottbooking.com>"  
ENV RESET_PASSWORD_URI="https://ottbooking.com"  
EXPOSE 3000  
CMD ["node", "/src/app.js"]  

