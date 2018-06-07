FROM openjdk:8  
ARG VERSION  
RUN wget -q https://downloads.typesafe.com/play/$VERSION/play-$VERSION.zip \  
&& unzip -q play-$VERSION.zip \  
&& rm play-$VERSION.zip \  
&& mv play-$VERSION /opt/play  
ENV PATH $PATH:/opt/play  

