FROM marmotz/nodejs  
  
USER root  
  
# Install Bower & Gulp  
RUN npm install -g bower gulp gulp-sass jspm  
  
ADD init_gulp.sh /  
  
USER nonrootuser  
  
VOLUME ["/data/app"]  
WORKDIR /data/app  
  
CMD ["/init_gulp.sh"]  

