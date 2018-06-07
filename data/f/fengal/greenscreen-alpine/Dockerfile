FROM alpine:3.5  
RUN apk add --no-cache --update nodejs git  
RUN git clone https://github.com/groupon/greenscreen.git /greenscreen  
RUN apk del git  
  
WORKDIR /greenscreen  
RUN npm install  
EXPOSE 4994  
ADD greenscreen.sh /greenscreen  
  
CMD ["sh", "/greenscreen/greenscreen.sh"]

