FROM 1science/sbt:0.13.8-oracle-jre-7  
MAINTAINER Nils Kuhn <nils.kuhn@iteratec.de>  
  
# install git  
RUN apk update  
RUN apk add git vim ruby ruby-dev  
# get rearview from git  
RUN git clone https://github.com/IteraSpeed/rearview.git --branch v1.0.0-scala
--single-branch /app  
# install mysql client  
RUN apk add mysql-client  
# create folder for ivy2 cache  
RUN mkdir /root/.ivy2  
# create volumes  
VOLUME /app/conf  
VOLUME /root/.ivy2  
  
EXPOSE 9000 8888  
ADD entrypoint.sh /root/entrypoint.sh  
RUN chmod u+x /root/entrypoint.sh  
CMD /root/entrypoint.sh

