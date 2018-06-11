FROM debian:stretch-slim  
MAINTAINER DJ Schleen <djschleen@gmail.com>  
  
ENV SERPICO_VERSION 1.2.1  
ENV ADMIN_PASSWORD admin  
  
RUN \  
apt-get update \  
&& apt-get install wget -y \  
&& wget
https://github.com/SerpicoProject/Serpico/releases/download/${SERPICO_VERSION}/serpico_${SERPICO_VERSION}_amd64.deb
\  
&& dpkg -i serpico_${SERPICO_VERSION}_amd64.deb  
  
RUN \  
apt-get remove wget -y \  
&& apt-get autoremove -y \  
&& rm serpico_${SERPICO_VERSION}_amd64.deb  
  
WORKDIR /opt/Serpico  
  
RUN \  
sed -i '/username = gets.chomp/c\ username = "administrator" '
Serpico/scripts/first_time.rb \  
&& sed -i '/user.password = password/c\ user.password = "admin"'
Serpico/scripts/first_time.rb \  
&& sed -i '/find_i = gets.chomp/c\ find_i = "Y"' Serpico/scripts/first_time.rb
\  
&& sed -i '/change = gets.chomp.downcase/c\ ' Serpico/scripts/manage_users.rb
\  
&& sed -i '/if change == "y" or change == ""/c\ if "y" == "y"'
Serpico/scripts/manage_users.rb  
# # # && sed -i '/ = username/c\ = "administrator"'
Serpico/scripts/first_time.rb  
EXPOSE 8443  
RUN ./init_serpico.sh  
  
VOLUME /opt/Serpico/Serpico/db /certs  
  
COPY scripts/launch.sh /launch.sh  
  
ENTRYPOINT ["/bin/sh", "-c", "/launch.sh" ]  

