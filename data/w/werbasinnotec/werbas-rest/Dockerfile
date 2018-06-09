FROM mhart/alpine-node:5.1.0  
MAINTAINER WERBAS Innotec <info@werbas-ag.com>  
  
RUN apk update  
  
RUN apk add \  
git \  
openssh \  
make \  
python  
  
COPY . /usr/share/werbas-rest  
WORKDIR /usr/share/werbas-rest  
  
RUN rm .git -r -f  
  
RUN npm install -g \  
gulp  
  
RUN npm install  
  
CMD ["gulp", "run"]  
  
EXPOSE 8080  

