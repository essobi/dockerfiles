FROM java:7  
MAINTAINER alex-glv  
ADD . /app  
WORKDIR /app  
ENV LEIN_ROOT true  
RUN curl
https://raw.githubusercontent.com/technomancy/leiningen/b630fa37b8b408c16ca86fdc5784e09dc889a612/bin/lein
\  
-o /usr/local/bin/lein \  
&& chmod a+x /usr/local/bin/lein && lein upgrade  
RUN /usr/local/bin/lein uberjar  
CMD ["java", "-cp","target/uberjar/stravinski-standalone-0.0.1.jar"]  

