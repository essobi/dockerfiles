# To build:  
# docker build -t cesaregb/laundry-web -f Dockerfile .  
# docker push cesaregb/laundry-web:v1  
#  
# To run:  
# run docker mongo....  
# docker run -p 3000:3000 -it cesaregb/laundry-web  
# docker run -p 3000:3000 -it --entrypoint bash interactivelabs/laundry-web  
FROM node:5.11  
MAINTAINER Cesar Gonzalez, cesareg.borjon@gmail.com  
  
# Install software  
RUN apt-get update && \  
apt-get install -y git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm set progress=false && \  
npm install --global --progress=false gulp bower && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Binary may be called nodejs instead of node  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN mkdir -p /root/.ssh  
ADD github_rsa /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config  
  
# RUN ssh-keyscan github.com >> ~/.ssh/github_rsa  
# Dependencies this needs to be commented when the script works  
ENV NODE_ENV=production  
ENV
VAULT='{"auth":{"facebook":{"clientId":"881601445289245","clientSecret":"8b3671fe28e22dd57b525d8cb864a2c9"}},"password":"wx8(rOqJIA^yok4aBv!(l25GjwHTP0g&","api":{"user":"user","password":"user"},"stripe":"sk_test_m1f9mBO7U4X1lDnerfKhTyK9"}'  
RUN mkdir app  
ADD . /app  
# COPY package.json app/package.json  
# COPY gulpfile.js app/gulpfile.js  
WORKDIR app  
RUN npm install --dev  
#RUN npm run build  
#Current workingdir is app from dependencies image.  
# ADD . /app  
# Define default command.  
ENTRYPOINT ["npm", "start"]  
# ENTRYPOINT ["start.sh"]  
# Expose ports.  
EXPOSE 3000  

