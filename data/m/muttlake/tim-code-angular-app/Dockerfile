#ng.Dockerfile  
#build stage  
FROM node as build  
RUN chown -R node:node /usr/local/lib/node_modules  
RUN chown -R node:node /usr/local/bin  
  
# node user gets created, use it to install npm  
USER node  
RUN npm install -g @angular/cli  
  
USER root  
WORKDIR /docker  
RUN git clone https://github.com/1803-mar12-net/tim-code.git  
RUN pwd  
RUN ls -lrt tim-code  
WORKDIR /docker/tim-code/Calculator/calculator  
RUN pwd  
RUN ls -lrt  
RUN npm install  
RUN ls -lrt  
RUN ng build  
RUN pwd  
RUN ls -lrt  
  
# #serve stage  
RUN echo "Now in serve stage"  
FROM nginx:1.12  
COPY \--from=build /docker/tim-code/Calculator/calculator/dist
/usr/share/nginx/html  
RUN pwd  
RUN ls -lrt  
EXPOSE 80  
# EOF  

