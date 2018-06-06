FROM google/golang:latest  
WORKDIR /root  
RUN go get -u github.com/cyfdecyf/cow  
RUN mkdir /root/.cow  
COPY rc /root/.cow/rc  
EXPOSE 10000  
CMD ["cow"]  

