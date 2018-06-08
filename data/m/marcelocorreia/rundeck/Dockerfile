FROM java:8  
RUN mkdir /usr/local/rundeck/  
WORKDIR /usr/local/rundeck  
RUN wget -c http://dl.bintray.com/rundeck/rundeck-maven/rundeck-
launcher-2.5.3.jar  
RUN useradd -g users -m -s /bin/bash yoda  
RUN chown -R yoda:users /usr/local/rundeck  
USER yoda  
WORKDIR /usr/local/rundeck  
CMD ["java","-jar","rundeck-launcher-2.5.3.jar"]  

