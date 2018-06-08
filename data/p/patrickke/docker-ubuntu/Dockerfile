FROM ubuntu:trusty-20150528  
MAINTAINER Ke Peng <kepeng1314@gmail.com>  
  
# Install packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
openssh-server pwgen vim wget sudo net-tools ca-certificates unzip \  
&& wget https://github.com/tianon/gosu/releases/download/1.4/gosu-amd64 -O
/usr/local/bin/gosu \  
&& chmod +x /usr/local/bin/gosu \  
&& rm -rf /var/lib/apt/lists/* # 20150604  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 22  
CMD ["/run.sh"]  
  

