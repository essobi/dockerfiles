  
FROM library/node  
MAINTAINER Iacopo <iac@pasixlab.com>  
  
RUN npm install -g bower grunt-cli && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
RUN useradd -u 1000 -md /home/iacopo iacopo  

