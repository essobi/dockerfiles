FROM robbertkl/node:latest  
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>  
  
# Set the locale  
#RUN localedef -i nl_NL -c -f UTF-8 -A /usr/share/locale/locale.alias
nl_NL.UTF-8  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :  
ENV LANG nl_NL.utf8  
#RUN locale-gen nl_NL.UTF-8  
#ENV LANG nl_NL.UTF-8  
#ENV LANGUAGE nl_NL:en  
#ENV LC_ALL nl_NL.UTF-8  
COPY package.json ./  
RUN npm install  
COPY . .  
  
ENTRYPOINT [ "node", "app" ]  
CMD []  

