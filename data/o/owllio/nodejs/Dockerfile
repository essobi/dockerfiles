FROM owllio/baseimage  
  
RUN apt-get install -y -q python pkg-config  
RUN git clone https://github.com/joyent/node.git  
  
RUN cd node && ./configure && make && make install  
# RUN rm -rf node  
RUN sudo apt-get install -y libpq-dev  
  
CMD node --harmony app.js  
  
WORKDIR /var/www  

