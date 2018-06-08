FROM node:6.5.0-onbuild  
ENV HOME /home/user  
RUN useradd --create-home --home-dir $HOME user \  
&& chown -R user:user /usr/src/app  
USER user  
  
CMD [ "npm", "start" ]  
  
EXPOSE 3000  

