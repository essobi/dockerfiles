FROM node:6  
MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV BUILDLSIT=""  
ENV APTLIST="supervisor"  
RUN apt-get update -q && \  
apt-get install $BUILDLIST $APTLIST -qy && \  
npm install --global gulp && \  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /root/.cache  
  
# problem with default version of the mongoose module so changing the
version...  
RUN git clone https://github.com/ExpediaInceCommercePlatform/cyclotron.git
/cyclotron && \  
cd /cyclotron/cyclotron-svc && \  
sed -i -e 's~"mongoose": .*$~"mongoose": "^4.7.1",~g' package.json && \  
npm install && \  
cd /cyclotron/cyclotron-site && \  
npm install && \  
gulp build  
  
ADD supervisord.conf /supervisord.conf  
CMD ["supervisord", "-c", "/supervisord.conf", "-n"]  

