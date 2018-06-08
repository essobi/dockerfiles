FROM haskell:8  
COPY . /opt/SeatRESTServer  
  
WORKDIR /opt/SeatRESTServer  
  
EXPOSE 8080  
RUN stack setup  
  
RUN stack build  
  
CMD ["stack","exec","SeatRESTServer-exe"]

