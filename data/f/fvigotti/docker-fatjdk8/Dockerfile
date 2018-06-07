FROM fvigotti/fatubuntu  
  
RUN cd /usr/local/src && \  
git clone https://github.com/fvigotti/bash-ubuntu-oraclejdk && \  
chmod +x /usr/local/src/bash-ubuntu-oraclejdk/src/install_oracle_jdk.sh && \  
chmod +x /usr/local/src/bash-ubuntu-oraclejdk/src/install_groovy.sh && \  
/bin/bash /usr/local/src/bash-ubuntu-oraclejdk/src/install_oracle_jdk.sh && \  
/bin/bash /usr/local/src/bash-ubuntu-oraclejdk/src/install_groovy.sh  
  
#WORKDIR /opt  
#ENTRYPOINT ["java", "-jar", "/whatever/your.jar"]  

