FROM java:8  
COPY * /opt/app/  
WORKDIR /opt/app  
  
ENTRYPOINT ["javac", "-Djava.security.egd=file:/dev/./urandom",
"Main.java;HelloLib.java"]  
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "Main"]  

