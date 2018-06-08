FROM irvui/alpine-node:4.4.3  
MAINTAINER Suhail Taj<suhailtajshaik@gmail.com>  
  
# Copy dist or your code folder to /opt/suhail folder in the container.  
COPY dist /opt/suhail  
  
# Switch to /opt/suhail as your working directory  
WORKDIR /opt/suhail  
  
# add a user named tspace and give read permissions to that user for
/opt/suhail folder and it's content.  
# Use below format to setup environment variables.  
ENV NODE_ENV=production PORT=9000 DEL_PKGS="libgcc libstdc++"
RM_DIRS=/usr/include  
  
# install packages, add tspace user and group,  
# install production npm packages,  
# delete packages that are no longer required for execution,  
# remove the directories that no long required,  
# finally setup read permissions to tspace user for /opt/suhail folder.  
RUN apk add \--no-cache curl make gcc g++ binutils-gold python linux-headers
paxctl libgcc libstdc++ gnupg && \  
adduser -S tspace && \  
addgroup -S tspace && \  
npm install \--unsafe-perm=true \--production && \  
apk del curl make gcc g++ binutils-gold python linux-headers paxctl gnupg
${DEL_PKGS} && \  
rm -rf rm -rf ${RM_DIRS} && \  
chown -R tspace:tspace /opt/suhail  
  
# install production npm packages.  
# RUN npm install --production  
# Set the tspace as the user to execute  
USER tspace  
  
# Expose port 9000 for accessing website from outside the container.  
EXPOSE 9000  
  
# Start your application when the container starts.  
CMD ["node", "server/server.js"]  
  

