FROM openjdk:8-jre  
WORKDIR /  
RUN wget -O cerebro.zip
https://github.com/lmenezes/cerebro/releases/download/v0.7.2/cerebro-0.7.2.zip
\  
&& unzip cerebro.zip \  
&& rm cerebro.zip \  
&& mv cerebro* cerebro  
WORKDIR /cerebro  
CMD ["java", "-jar", "/cerebro/lib/cerebro.cerebro-0.7.2-launcher.jar"]  

