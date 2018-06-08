###########################################################  
# Dockerfile for creating a self-hosting version of  
# tfk-form-skoleskyss  
###########################################################  
  
# Setting the base to iojs  
FROM iojs  
  
# Maintainer  
MAINTAINER Geir Gåsodden  
  
#### Begin setup ####  
  
# Clone the repo  
RUN git clone https://github.com/telemark/tfk-form-skoleskyss.git skoleskyss  
  
# Change working directory  
WORKDIR "/skoleskyss"  
  
# Run the setup script  
RUN npm run setup  
  
# Expose  
EXPOSE 3000  
  
# Startup  
ENTRYPOINT node standalone.js

