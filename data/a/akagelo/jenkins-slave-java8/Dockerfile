# Version: 0.0.1  
FROM debian:jessie-backports  
MAINTAINER Oleg Vyukov <gelo@vyukov.ru>  
  
  
RUN echo "deb http://httpredir.debian.org/debian/ jessie-backports main
contrib non-free" > /etc/apt/sources.list.d/backports.list && \  
echo "deb http://httpredir.debian.org/debian/ jessie main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb http://httpredir.debian.org/debian/ jessie-updates main contrib non-
free" >> /etc/apt/sources.list &&\  
echo "deb http://security.debian.org jessie/updates main contrib non-free" >>
/etc/apt/sources.list  
  
# обновляшки  
RUN apt-get update  
  
#минимально необходимое для jenkins  
RUN apt-get install -y wget git openjdk-8-jdk openssh-server  
  
RUN mkdir -p /var/run/sshd  
RUN chmod 0755 /var/run/sshd  
  
# создает пользователя для дженкинса  
RUN useradd -ms /bin/bash jenkins  
  
# стандартный пароль, так как слейвы предназначены для использования в
приватной сети  
RUN echo "jenkins:jenkins" | chpasswd  
  
#копируем самопальную систему иннициализации  
ADD etc/ /etc/  
ADD start.sh /start.sh  
  
#отключаем проверку хостов в ssh  
RUN mkdir -p /home/jenkins/.ssh/ && echo "Host * \r\n StrictHostKeyChecking
no" > /home/jenkins/.ssh/config && chown -R jenkins:jenkins
/home/jenkins/.ssh/  
  
# SSH port  
EXPOSE 22  
CMD ["bash", "/start.sh"]

