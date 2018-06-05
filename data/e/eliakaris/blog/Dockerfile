FROM node  
WORKDIR /usr/src/app  
  
# ------------------------  
# SSH Server support  
# ------------------------  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends openssh-server \  
&& echo "root:Docker!" | chpasswd  
  
COPY ssh/sshd_config /etc/ssh/  
  
COPY bin/init.sh bin/  
RUN chmod 755 bin/init.sh  
  
COPY package*.json ./  
RUN npm install  
  
COPY . .  
  
ENV CI True  
RUN npm test  
  
RUN npm run build  
  
ENV PORT 80  
EXPOSE 2222 80  
CMD [ "bash", "/usr/src/app/bin/init.sh" ]  

