FROM node:latest  
  
RUN useradd --user-group --create-home --shell /bin/false app  
  
ENV HOME=/home/app  
ENV APP=historicalbattles  
  
WORKDIR $HOME  
  
COPY . $HOME/$APP/  
  
RUN chown -R app:app $HOME/*  
  
USER app  
WORKDIR $HOME/$APP  
RUN npm install  
  
EXPOSE 8080  
ENTRYPOINT [ "npm" ]  
CMD [ "start" ]  
  

