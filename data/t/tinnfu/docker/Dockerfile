FROM tinnfu/docker:latest  
  
MAINTAINER tinnfu <tinnfu@gmail.com>  
  
USER root  
  
# correct time  
RUN echo 'Asia/Shanghai' > /etc/timezone  
RUN cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# add user and set passwd  
RUN echo 'root:root' | chpasswd  
RUN if [ ! $(grep '^admin' /etc/passwd | wc -l) ]; then $(useradd admin &&
echo 'admin:admin' | chpasswd && mkdir -p /home/admin/ && chown admin:admin
/home/admin); fi  
  
# add env script  
ADD env.tgz /home/admin/  
  
# add source  
RUN if [ ! $(grep 163 /etc/apt/sources.list | wc -l) ]; then $(cp -f
/etc/apt/sources.list /home/admin/sources.list.back && cp -f
/home/admin/sources.list /etc/apt/sources.list && cat
/home/admin/sources.list.back >> /etc/apt/sources.list); fi  
  
# install work-tool  
RUN apt-get update  
RUN apt-get install python -y  
RUN apt-get install vim -y  
RUN apt-get install git -y  
RUN apt-get install gcc -y  
RUN apt-get install g++ -y  
RUN apt-get install gdb -y  
RUN apt-get install pstack -y  
RUN apt-get install tree -y  
RUN apt-get install inetutils-ping -y  
RUN apt-get install net-tools -y  
RUN apt-get install tmux -y  
RUN apt-get install wget -y  
RUN apt-get install curl -y  
RUN apt-get install man -y  
RUN apt-get install iptables -y  
RUN apt-get install netcat -y  
RUN apt-get install openssh-server -y  
  
# set env  
WORKDIR /home/admin  
ENV SHELL /bin/bash  
  
# switch to admin  
USER admin  
  
VOLUME /home/admin/vdisk  
  
CMD ["/bin/bash"]  

