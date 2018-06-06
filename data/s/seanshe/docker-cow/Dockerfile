FROM alpine  
MAINTAINER sean  
  
  
  
RUN rm -Rf ~/.cow  
RUN rm -Rf /app  
RUN mkdir ~/.cow  
RUN mkdir /app  
  
COPY cow/cow /app/  
COPY start.sh /app/  
  
WORKDIR /app  
RUN chmod +x start.sh && chmod +x cow  
  
VOLUME /cowconfig  
  
CMD ["./start.sh"]

