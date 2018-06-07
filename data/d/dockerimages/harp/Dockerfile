FROM node:5.1  
ENV DOCKER_BUILD docker build -t dockerimages/blog_dspeed
git://github.com/dockerimages/harp-git  
ENV DOCKER_RUN docker run -d --restart=always --name=WEB_blog.dspeed.eu -v
/var/www:/var/www dockerimages/docker-harp  
ENV NODE_ENV production  
RUN npm install -g harp  
VOLUME /var/www  
COPY index.md /var/www/index.md  
WORKDIR /var/www  
EXPOSE 80  
CMD harp server /var/www --port 80  

