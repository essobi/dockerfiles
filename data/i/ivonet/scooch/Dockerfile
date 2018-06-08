FROM node  
MAINTAINER IvoNet <webmaster@ivonet.nl>  
ENV TAG 2.5.6  
RUN git clone -b $TAG \--single-branch https://github.com/IvoNet/scooch.git  
WORKDIR /scooch  
RUN npm install --production && ln -s /scooch/slides /slides && ln -s
/scooch/templates /templates  
EXPOSE 3000  
VOLUME /slides  
VOLUME /templates  
ENTRYPOINT npm start

