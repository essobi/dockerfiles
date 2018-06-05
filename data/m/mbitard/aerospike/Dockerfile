FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
  
#Runit  
RUN apt-get install -y runit  
CMD /usr/sbin/runsvdir-start  
  
#Utilities  
RUN apt-get install -y vim less net-tools inetutils-ping curl git telnet nmap
socat dnsutils netcat tree htop unzip sudo software-properties-common  
  
#Aerospike  
RUN curl -L http://www.aerospike.com/download/server/3.3.9/artifact/ubuntu12 |
tar xz  
  
#Init instance  
RUN cd aerospike* && dpkg -i *.deb  
# sed -i "s|run-as-daemon|run-as-daemon false|" /aerospike-
server/instance/etc/aerospike.conf  
#AMC  
RUN apt-get install -y build-essential python-dev python-pip man wget  
RUN wget -O aerospike-amc.deb
http://www.aerospike.com/download/amc/3.4.5/artifact/ubuntu12  
RUN dpkg -i aerospike-amc*.deb  
  
#Configure aerospike  
RUN sed -i "s|proto-fd-max 15000|proto-fd-max 1024|"
/etc/aerospike/aerospike.conf  
  
#Add runit services  
ADD sv /etc/service  
  

