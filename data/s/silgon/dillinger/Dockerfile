# usage:  
# docker run --rm -p 8080:8080 dillinger  
FROM node:latest  
  
ENV PORT 8080  
ENV HOME /home/dillinger  
RUN useradd --create-home --home-dir $HOME dillinger  
WORKDIR $HOME  
  
RUN git clone https://github.com/joemccann/dillinger.git &&\  
cd dillinger &&\  
npm install -d  
  
EXPOSE $PORT  
  
RUN chown -R dillinger:dillinger $HOME  
USER dillinger  
  
CMD cd dillinger && node app  

