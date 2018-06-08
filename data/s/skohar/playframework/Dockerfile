FROM skohar/playframework:2.4.6  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ONBUILD COPY . /usr/src/app/  
ONBUILD RUN sbt update  

