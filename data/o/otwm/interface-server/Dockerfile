FROM node  
MAINTAINER dong o kim <otwmoo@gmail.com>  
  
RUN \  
mkdir -p /app/src && \  
mkdir -p /app/resource  
  
ADD ./ /app/src/  
  
WORKDIR /app/src  
  
RUN \  
apt-get update #&& \  
RUN \  
apt-get install -y software-properties-common #&& \  
RUN \  
add-apt-repository -y ppa:dhor/myway #&& \  
RUN \  
apt-get install -y graphicsmagick #&& \  
RUN \  
npm install #&& \  
RUN \  
npm run build  
  
VOLUME ["/app/resource"]  
  
#WORKDIR /app/src  
  
CMD ["npm", "start"];  

