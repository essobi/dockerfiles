# usage:  
# docker run --rm -p 3001:3001 -p 1987:1987 silgon/tyto  
FROM node:latest  
  
ENV HOME /home/tyto  
RUN useradd --create-home --home-dir $HOME tyto  
WORKDIR $HOME  
RUN git clone https://github.com/jh3y/tyto.git  
RUN cd tyto && npm install  
  
RUN npm install -g bower  
RUN npm install -g gulp  
RUN cd tyto && bower install --allow-root  
EXPOSE 3001 1987  
RUN chown -R tyto:tyto $HOME  
USER tyto  
CMD cd tyto && gulp  

