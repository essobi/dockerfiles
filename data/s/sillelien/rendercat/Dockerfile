FROM sillelien/rendercat-base  
MAINTAINER Neil Ellis hello@neilellis.me  
  
# Set working directory.  
ENV HOME /root  
WORKDIR /root  
  
# Env  
ENV SLIMERJS_VERSION_M 0.9  
ENV SLIMERJS_VERSION_F 0.9.4  
#ENV PHANTOM_VERSION 1.9.7  
RUN apt-get install -y supervisor firefox  
RUN mkdir -p /app/public/_rendered/  
  
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
ADD lib/render.js /usr/local/lib/  
  
##Xvfbd  
#ADD bin/xvfb /etc/init.d/xvfb  
#RUN chmod +x /etc/init.d/xvfb  
#RUN update-rc.d xvfb defaults  
# Remove the default Nginx configuration file  
RUN rm -v /etc/nginx/nginx.conf  
  
# Removed unnecessary packages  
RUN apt-get autoremove -y  
  
# Clear package repository cache  
RUN apt-get clean all  
  
WORKDIR /app  
ADD package.json /app/  
RUN npm install  
  
COPY etc/fonts.conf /root/.fonts.conf  
  
ADD public/ /app/public  
ADD routes/ /app/routes  
ADD views/ /app/views  
ADD bin/ /app/bin  
ADD app.js /app/  
ADD RenderCat.js /app/  
ADD modules/ /app/modules  
ADD run.sh /app/  
ADD gulpfile.js /app/  
  
#Etc  
ADD lib/render.js /usr/local/lib/  
  
#Bin  
ADD bin/phantom_or_slimer.sh /usr/local/bin/phantom_or_slimer  
ADD bin/render_params.sh /usr/local/bin/render_params.sh  
ADD bin/cuty.sh /usr/local/bin/cuty  
ADD bin/poller /usr/local/bin/poller  
ADD bin/runner /usr/local/bin/runner  
ADD bin/render /usr/local/bin/render  
ADD bin/convert.sh /usr/local/bin/convert.sh  
ADD bin/cleanup.sh /usr/local/bin/cleanup.sh  
COPY etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN chmod 755 /usr/local/bin/*  
  
COPY etc/nginx.conf /etc/nginx/nginx.conf  
  
RUN chmod 755 /app/run.sh  
  
RUN node /app/gulpfile.js  
  
EXPOSE 80  
EXPOSE 3000  
CMD ["/usr/bin/supervisord"]  
  
ONBUILD COPY modules/ /app/modules/  
ONBUILD COPY public/ /app/public/  

