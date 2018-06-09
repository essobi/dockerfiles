FROM fjukstad/seqbase  
  
WORKDIR /tools  
RUN wget
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip  
RUN unzip Trimmomatic-0.36  
RUN mv Trimmomatic-0.36 trimmomatic  
  
USER worker  
  
ENTRYPOINT ["java", "-jar","/tools/trimmomatic/trimmomatic-0.36.jar"]  

