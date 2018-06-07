FROM gradle:4.7 AS BUILD  
  
RUN wget -q https://github.com/vmk/rite/archive/master.tar.gz  
RUN tar xzf master.tar.gz  
  
WORKDIR /home/gradle/rite-master  
RUN gradle installDist  
  
FROM evidence/newsreaderdutch  
  
COPY \--from=BUILD /home/gradle/rite-master/build/install/rite /rite  
ENTRYPOINT [ "/rite/bin/rite" ]  

