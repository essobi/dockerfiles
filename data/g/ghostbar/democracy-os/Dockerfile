FROM node:argon  
MAINTAINER Jose-Luis Rivas <me@ghostbar.co>  
  
ENV NODE_PATH=.  
ENV DEBUG=democracyos*  
  
WORKDIR /opt/app  
  
RUN git clone git://github.com/DemocracyOS/democracyos /opt/app && \  
npm install --quiet && \  
make build  
  
EXPOSE 3000  
CMD ["make", "run"]  

