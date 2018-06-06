FROM openjdk:9  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN groupadd --gid 1000 java \  
&& useradd --uid 1000 --gid java --shell /bin/bash --create-home java  
  
RUN chown -R java:java /usr/local  
  
USER java  
WORKDIR /home/java  
  
ENTRYPOINT ["/bin/bash"]

