FROM cazcade/rendercat-base  
MAINTAINER Neil Ellis neil@cazcade.com  
  
# Set working directory.  
ENV HOME /root  
WORKDIR /root  
  
# Env  
ENV SLIMERJS_VERSION_M 0.9  
ENV SLIMERJS_VERSION_F 0.9.0  
ENV PHANTOM_VERSION 1.9.7  
## CasperJS  
# RUN git clone https://github.com/n1k0/casperjs.git /usr/local/casperjs  
# RUN echo '#!/bin/bash\n/usr/local/casperjs/bin/casperjs --engine=slimerjs
$*' > /usr/local/casperjs/casperjs.sh  
# RUN chmod 755 /usr/local/casperjs/casperjs.sh  
# RUN ln -s /usr/local/casperjs/casperjs.sh /usr/bin/casperjs  
##For polling and running  
#RUN apt-get -y update  
#RUN apt-get install -y redis-server moreutils  
#RUN rm /etc/parallel/config  
#Etc  
#ADD lib/render.js /usr/local/snapito/lib/  
#Flash  
RUN apt-get install -y flashplugin-installer  
  
#CutyCapt  
RUN apt-get install -y cutycapt  
  
#Git Related  
RUN curl
https://raw.githubusercontent.com/progrium/gitreceive/master/gitreceive >
/usr/local/bin/gitreceive  
RUN chmod 755 /usr/local/bin/gitreceive  
RUN /usr/local/bin/gitreceive init  
  
#Xvfbd  
ADD bin/xvfb /etc/init.d/xvfb  
RUN chmod +x /etc/init.d/xvfb  
RUN update-rc.d xvfb defaults  
  
# Install Nginx  
# Download and Install Nginx  
RUN apt-get install -y nginx  
  
# Remove the default Nginx configuration file  
RUN rm -v /etc/nginx/nginx.conf  
  
# Removed unnecessary packages  
RUN apt-get autoremove -y  
  
# Clear package repository cache  
RUN apt-get clean all  
  
# Node stuff  
RUN npm install forever -g  
  
WORKDIR /app  
ADD package.json /app/  
RUN npm install  
  
ADD public/ /app/public  
ADD routes/ /app/routes  
ADD views/ /app/views  
ADD bin/ /app/bin  
ADD app.js /app/  
ADD RenderCat.js /app/  
ADD rendercat_modules/ /app/rendercat_modules  
ADD run.sh /app/  
ADD gulpfile.js /app/  
  
ADD etc/nginx.conf /etc/nginx/  
# Append "daemon off;" to the beginning of the configuration  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN chmod 755 /app/run.sh  
  
RUN node /app/gulpfile.js  
  
EXPOSE 80  
EXPOSE 3000  
#CMD forever --watchDirectory rendercat_modules app.js  
CMD /app/run.sh  

