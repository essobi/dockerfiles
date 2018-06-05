FROM php:5.6  
# Install dependencies  
RUN sh -c 'echo "deb http://www.deb-multimedia.org jessie main" >>
/etc/apt/sources.list'  
RUN apt-get update  
RUN apt-get install --force-yes -y ffmpeg git  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create application folder  
RUN mkdir /app  
  
# Download banana-split  
RUN git clone https://github.com/pathartl/banana-split /app  
  
# Copy startup script  
COPY start.sh /app/  
  
# Start application  
WORKDIR /app  
CMD ./start.sh  
  
# Declare application port  
EXPOSE 8080  

