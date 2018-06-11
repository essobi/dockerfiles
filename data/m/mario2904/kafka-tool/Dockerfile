FROM openjdk:jre  
  
WORKDIR /root  
  
RUN wget http://www.kafkatool.com/download/kafkatool.sh  
RUN chmod +x kafkatool.sh  
  
# Handle noninteractive installation  
RUN printf "\n\n\n\n\n\n1\n\n\n\n" | ./kafkatool.sh  
  
CMD ["kafkatool"]  

