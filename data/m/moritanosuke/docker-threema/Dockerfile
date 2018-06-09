FROM node:7.5.0  
RUN git clone \--branch v1.0.1 https://github.com/threema-ch/threema-web.git  
RUN cd threema-web && npm install  
  
WORKDIR threema-web  
CMD ["npm", "run", "serve:live"]  

