FROM library/ubuntu  
FROM library/openjdk  
FROM frekele/gradle  
  
ADD . digitrecognizer/  
  
RUN cd digitrecognizer && gradle build  
RUN chmod +x ./digitrecognizer/run.sh  
  
CMD ./digitrecognizer/run.sh

