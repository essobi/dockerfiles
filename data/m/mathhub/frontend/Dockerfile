# We need a node image with yarn  
FROM node as builder  
  
# The URL to MMT to use in the build  
ARG MMT_URL="/:mathhub/"  
ARG MOCK_MMT=""  
# Add all of the app into /app/  
ADD assets/ /app/assets/  
ADD build/ /app/build  
ADD src/ app/src/  
ADD .babelrc /app/  
ADD LICENSE.txt /app/  
ADD package.json /app/  
ADD tsconfig.json /app/  
ADD webpack.config.js /app/  
ADD webpack.config.prod.js /app/  
ADD tslint.json /app/  
ADD yarn.lock /app/  
  
# Install and run build  
WORKDIR /app/  
RUN yarn \  
&& MMT_URL=${MMT_URL} MOCK_MMT=${MOCK_MMT} yarn webpack
--config=webpack.config.prod.js \  
&& yarn --ignore-platform licenses generate-disclaimer > dist/NOTICES.txt  
  
# And place onto a static server  
FROM pierrezemb/gostatic:latest  
COPY \--from=builder /app/dist/ /srv/http  
EXPOSE 8043  

