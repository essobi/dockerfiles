# Select source image  
FROM
node:wheezy@sha256:4e94d7eab2c3c8c59647b534699c32c5cbcdce371e70eb314c2d056922b2a2f1  
  
# Install all dependencies  
RUN apt-get update -q && apt-get upgrade -y --no-install-recommends  
  
# Create app directories  
RUN mkdir -p /usr/app/config  
WORKDIR /root  
  
# We download the eae interface  
RUN git clone -b master https://github.com/dsi-icl/eae-interface  
  
WORKDIR /root/eae-interface  
  
# Bundle app  
RUN cp package.json /usr/app/ \  
&& cp -r src /usr/app/src  
  
WORKDIR /usr/app  
  
# Install eae-interface npm dependencies  
RUN npm install --silent; exit 0;  
RUN cat /root/.npm/_logs/*; exit 0;  
  
# Run interface service  
EXPOSE 80  
CMD [ "npm", "start" ]  

