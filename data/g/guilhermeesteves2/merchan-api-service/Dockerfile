FROM node  
  
# Create app directory  
RUN mkdir -p /usr/src/aplication  
WORKDIR /usr/src/aplication/  
  
# Setando variavel  
ENV HTTPSERVER="TRUE"  
ENV PORT=18203  
ENV APIGEEURL="https://stage.apiluiza.com.br/v1"  
ENV CODIGOSISTEMA="3808"  
ENV APIGEEAUTHTOKEN="Bearer 185uqNPIX5LJJ2czAiF2wAnGWGgx"  
ENV MERCHANTOKEN="MDk2NTE4N2HORNETFhMjMzODc5NGMwYWVlN2U5NGExM2FmM2MTR4NS4"  
# Install app dependencies  
COPY package.json /usr/src/aplication/  
RUN npm -y install  
  
# Bundle app source  
COPY app.js /usr/src/aplication  
COPY app /usr/src/aplication/app  
  
EXPOSE 18203  
CMD ["node", "app.js"]  

