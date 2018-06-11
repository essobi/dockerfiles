FROM node:6-slim  
  
ENV ELM="0.18.0" WEBPACK="3.10.0" BABEL="6.26.0" UGLIFY="3.3.9"  
RUN npm install -g "elm@$ELM" \  
&& npm install -g "elm-test@$ELM" \  
&& npm install -g "babel-cli@$BABEL" \  
&& npm install -g "uglify-js@$UGLIFY" \  
&& npm install -g "webpack@$WEBPACK"  
  
CMD ["elm"]  
  

