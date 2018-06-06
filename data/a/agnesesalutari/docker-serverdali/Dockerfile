FROM tutum/apache-php  
MAINTAINER Agnese Salutari  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get install -y libc6-i386 && apt-get install -y lib32ncurses5 && apt-
get install -y lib32stdc++6 && apt-get install -y vim && apt-get install -y
build-essential && apt-get -y install wget git  
  
RUN git clone git://github.com/agnsal/ServerDALI && git clone
git://github.com/AAAI-DISIM-UnivAQ/DALI && git clone
git://github.com/agnsal/ServerDALImas  
  
RUN cp -a DALI ServerDALI/ && rm -r -f DALI && cp -a ServerDALImas
ServerDALI/DALI/ && rm -r -f ServerDALImas && cd
ServerDALI/DALI/ServerDALImas/conf && mkdir mas  
  
EXPOSE 80/tcp  
EXPOSE 3306/tcp  

