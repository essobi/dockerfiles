###  
# Node.js app Docker file  
#  
# Some basic build instructions:  
# ```  
# # you should delete node_modules b/c you don't want that copied during 'ADD'  
# docker build -t thom-nic/node-bootstrap .  
# # run a shell in the container to inspect the environment (as root):  
# docker run --rm -itu root thom-nic/node-bootstrap /bin/bash  
# ```  
###  
FROM wolfhesse/nodejs  
MAINTAINER @wolfhesse "wolfgang.schuessel@gmail.com"  
LABEL dockerfile_version="0.34.0"  
  
USER root  
RUN apt-get update  
RUN apt-get install -y telnet nmap screen tmux wget htop sudo  
RUN useradd -ms /bin/bash rogera  
  
RUN echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf  
  
# copy the nice dotfiles that dockerfile/ubuntu gives us:  
# RUN cd && cp -R .bash_profile .bashrc .gitconfig .profile scripts
/home/rogera  
#RUN npm install -g grunt-cli  
#RUN npm install -g bower  
RUN rm -r /tmp/*  
RUN chown -R rogera:rogera /home/rogera  
  
USER rogera  
ENV HOME /home/rogera  
ENV SERVER code-wolfhesse.c9.io  
ENV SERVER_PORT 8080  
EXPOSE 44000  
ADD ./src /home/rogera/app  
  
WORKDIR /home/rogera/app  
  
#ENV NODE_ENV production  
#RUN npm install --ca=null  
## geht nicht bei docker build ...  
#RUN npm update  
#CMD ["npm", "start"]  
CMD ["node", "app"]  
  
#ENV DEBIAN_FRONTEND noninteractive  
#COPY node /srv/  
#EXPOSE 4000  
#USER default  
#WORKDIR /srv  
#CMD ["/srv/commander.js"]  
#ENTRYPOINT ["forever"]  

