FROM node:5-onbuild  
ENV TZ=Asia/Kolkata  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Create app directory  
RUN mkdir -p /root/wbas/src/wbasapp  
WORKDIR /root/wbas/src/wbasapp  
  
# Install app dependencies  
COPY package.json /root/wbas/src/wbasapp/  
RUN npm install  
  
# Bundle app source  
COPY . /root/wbas/src/wbasapp  
  
EXPOSE 8000  
CMD [ "npm", "start" ]

