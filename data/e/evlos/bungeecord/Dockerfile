FROM evlos/openjdk7  
  
MAINTAINER Evlos <4tyle8@gmail.com>  
  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install openssh-server supervisor  
  
RUN mkdir -p /app && \  
mkdir -p /root/.ssh && \  
mkdir -p /var/run/sshd && \  
sed -i "s/#PasswordAuthentication.*/PasswordAuthentication no/"
/etc/ssh/sshd_config && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \  
cd /app && \  
wget
"http://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar"  
  
ADD supervisord.conf /app/supervisord.conf  
ONBUILD ADD config.yml /app/config.yml  
ONBUILD ADD authorized_keys /root/.ssh/authorized_keys  
ONBUILD RUN chown root:root /root/.ssh/authorized_keys && chmod 600
/root/.ssh/authorized_keys  
ONBUILD ADD server-icon.png /app/server-icon.png  
  
EXPOSE 22  
EXPOSE 25565  
WORKDIR /app  
CMD ["/usr/bin/supervisord"]  

