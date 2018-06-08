FROM strongloop/node  
  
# You start off as the 'strongloop' user.  
# If a RUN command needs root, you can use sudo  
# In addition to standard Linux commands you also have access to node, npm,  
# and slc commands  
# It is common to copy your current  
ADD . /home/strongloop/medici-roar  
WORKDIR /home/strongloop/medici-roar  
# RUN npm install  
ENV NODE_ENV production  
CMD [ "slc", "run", "." ]  

