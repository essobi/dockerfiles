FROM node:alpine  
MAINTAINER Will Hall <will@willhallonline.co.uk>  
  
# Get required stylelint packages  
RUN npm install -g stylelint stylelint-config-standard  
  
# Setup stylelint entrypoint and default styleint  
COPY ./.stylelintrc /root/.stylelintrc  
COPY ./stylelint.sh /root/stylelint.sh  
RUN chmod +x /root/stylelint.sh  
  
WORKDIR /app  
  
# Entrypoint for creation of .stylelintrc if not in existence  
ENTRYPOINT ["/root/stylelint.sh"]  

