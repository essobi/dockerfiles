FROM pluswerk/puppeteer  
  
WORKDIR /app  
  
RUN yarn add convert-svg-to-png express body-parser  
  
COPY index.mjs /app/  
  
CMD ["node", "--experimental-modules", "index.mjs"]  
  
EXPOSE 3000  

