FROM ubuntu:16.04  
MAINTAINER YHSPY "yhorg@hotmail.com"  
ENV REFRESHED_AT 2017-11-15  
ENV HOME /home  
LABEL version="1.0"  
LABEL description="A common nodejs environment."  
ARG PROJECT_ROOT  
WORKDIR ${HOME}  
RUN apt-get -yqq update && apt-get -yqq install curl wget gcc g++ python make  
RUN apt-get -yqq install ssh vim sed  
RUN wget -O node.bundle https://nodejs.org/dist/v8.9.1/node-v8.9.1.tar.gz  
RUN tar -xvzf node.bundle  
WORKDIR ${HOME}/node-v8.9.1  
RUN ./configure && make -j4 && make install  
RUN echo "Node Version:" $(node --version) ", NPM Version" $(npm --version)  
# ssh  
RUN sed -i "s/PermitRootLogin prohibit-password/PermitRootLogin yes/g"
/etc/ssh/sshd_config  
RUN service ssh start  
WORKDIR ${HOME}  
RUN rm -rf ${HOME}/node-v8.9.1 && rm -rf ${HOME}/node.bundle  
RUN echo ${PROJECT_ROOT}  
ADD ${PROJECT_ROOT} ${HOME}/  
RUN echo $'#!/bin/bash\n\  
service ssh start\n'\  
>> /etc/init.d/docker_startup.sh  
CMD ["sh", "-c", "echo root:${ENV_PASS} | /usr/sbin/chpasswd; service ssh
start; /bin/bash"]  
EXPOSE 80 22 3000  

