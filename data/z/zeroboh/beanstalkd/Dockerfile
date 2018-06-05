FROM alpine:3.4  
ADD install.sh install.sh  
RUN chmod +x install.sh && sleep 1 && ./install.sh && rm install.sh  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300"]

