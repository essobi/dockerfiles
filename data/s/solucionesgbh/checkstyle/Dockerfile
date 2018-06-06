FROM openjdk:8  
RUN apt-get update -yqq && apt-get install -yqq curl  
  
RUN curl -L
https://downloads.sourceforge.net/project/checkstyle/checkstyle/8.0/checkstyle-8.0-all.jar
> /checkstyle.jar  
  
ADD checkstyle.sh /usr/bin/checkstyle  
RUN chmod +x /usr/bin/checkstyle  

