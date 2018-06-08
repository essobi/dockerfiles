FROM gotchas/pharo-teapot  
MAINTAINER Christer Assmundsson  
  
EXPOSE 1701  
  
ADD . ./deploy  
  
#CMD ./pharo Pharo.image ./deploy/zinc.st  
#CMD ./pharo Pharo.image ./deploy/seaside.st  
RUN ./pharo Pharo.image ./deploy/main.st  

