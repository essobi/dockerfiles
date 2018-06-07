FROM hermeto/opfox:latest  
  
RUN apt update; \  
apt upgrade -y; \  
apt install mysql-client -y; \  
apt install pv -y; \  
apt install ruby-full -y; \  
gem install sass  
  
RUN DEBIAN_FRONTEND="noninteractive" echo "America/Sao_Paulo" > /etc/timezone
&& dpkg-reconfigure -f noninteractive tzdata  

