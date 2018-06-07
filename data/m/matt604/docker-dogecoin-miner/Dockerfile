#  
# I don't use this, but fill your boots!  
FROM ubuntu:13.10  
MAINTAINER Matt Sawasy, sawasy@gmail.com  
  
# Some defaults that won't work  
ENV URL stratum+tcp://stratum.dogestylemining.org:943  
ENV USERNAME username  
ENV PASSWORD password  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget tar rsyslog  
  
#Get the miner  
RUN wget -O /root/pooler-cpuminer-2.3.3-linux-x86_64.tar.gz
http://sourceforge.net/projects/cpuminer/files/pooler-
cpuminer-2.3.3-linux-x86_64.tar.gz  
RUN tar xfz /root/pooler-cpuminer-2.3.3-linux-x86_64.tar.gz -C /root/  
ADD start-miner /root/start-miner  
RUN chmod u+x /root/start-miner  
  
CMD ["/root/start-miner"]  

