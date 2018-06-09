FROM anapsix/alpine-java:9  
RUN apk update  
  
RUN apk add ca-certificates wget  
RUN update-ca-certificates  
RUN wget
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein  
RUN chmod a+x lein  
RUN mv lein /usr/local/bin/  
RUN lein version  

