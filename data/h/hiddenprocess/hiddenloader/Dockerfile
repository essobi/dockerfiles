FROM mkenney/npm:alpine  
MAINTAINER Tailchakra  
  
# Expose port  
EXPOSE 1730  
# Make ssh dir  
RUN mkdir /root/.ssh/  
  
# Copy over private key, and set permissions  
ADD id_rsa /root/.ssh/id_rsa  
RUN chmod 600 /root/.ssh/id_rsa  
  
# Create known_hosts  
RUN touch /root/.ssh/known_hosts  
# Add bitbuckets key  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
  
# Clone  
RUN git clone git@bitbucket.org:hiddenprocess/hiddenloader.git HiddenLoader \  
&& mv HiddenLoader/app / \  
&& rm -R HiddenLoader  
  
# Finish  
WORKDIR /app  
RUN ["npm", "install"]  
CMD ["node", "app.js"]  
VOLUME ["/downloads"]

