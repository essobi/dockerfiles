FROM mhart/alpine-node:6.14.2  
  
RUN apk update && apk upgrade && apk add \--no-cache git  
  
RUN npm install frontail@4.2.0 --global  
  
ENTRYPOINT ["frontail"]  
EXPOSE 9001  
CMD ["--help"]  

