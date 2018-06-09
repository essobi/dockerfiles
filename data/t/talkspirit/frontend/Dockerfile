FROM node:10.1.0  
# to build package  
RUN apt-get update && apt-get install -y build-essential debhelper devscripts
vim curl  
# cypress  
RUN apt-get install -y xvfb libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3
libxss1 libasound2  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chown node.node /entrypoint.sh  
  
ENTRYPOINT ["sh", "/entrypoint.sh"]  
CMD ["bash"]  

