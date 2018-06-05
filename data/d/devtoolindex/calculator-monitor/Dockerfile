FROM java:openjdk-8u111  
  
ENV calculator_monitor_version 3.0.1  
RUN mkdir -p /usr/src/myapp  
  
WORKDIR /usr/src/myapp  
  
RUN wget https://jitpack.io/com/github/dev-tool-index/calculator-
monitor/${calculator_monitor_version}/calculator-
monitor-${calculator_monitor_version}.jar -O /usr/src/myapp/calculator-
monitor.jar  
  
EXPOSE 8080  
CMD ["java", "-jar", "/usr/src/myapp/calculator-monitor.jar"]  

