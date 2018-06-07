FROM node:5  
RUN mkdir -p /usr/local/webp \  
&& curl -SL
http://downloads.webmproject.org/releases/webp/libwebp-0.4.4-rc2-linux-x86-64.tar.gz
\  
| tar -xz -C /usr/local/webp  
  
ENV PATH /usr/local/webp/libwebp-0.4.4-rc2-linux-x86-64/bin:$PATH  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
  
EXPOSE 8080  
CMD [ "npm", "start" ]

