  
FROM node  
USER root  
  
WORKDIR /root  
  
# Get sources  
# Make sure the correct branch/release is used here!  
RUN git clone https://github.com/data-intuitive/LuciusWeb  
  
# LuciusWeb  
RUN cd /root/LuciusWeb \  
&& npm install  
  
# Port to expose  
EXPOSE 8080  
# RUN  
CMD cd /root/LuciusWeb && npm run serve  

