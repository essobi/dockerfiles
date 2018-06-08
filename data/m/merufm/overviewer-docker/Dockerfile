FROM debian:jessie  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get dist-upgrade -y  
RUN apt-get -y install build-essential python-imaging python-dev python-numpy
git  
WORKDIR /overviewer  
RUN git clone https://github.com/overviewer/Minecraft-Overviewer.git
/overviewer  
RUN python setup.py build  
RUN apt-get install -y nginx  
RUN apt-get install -y imagemagick  
# Append "daemon off;" to the beginning of the configuration  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Expose ports  
EXPOSE 80  
# Set the default command to execute  
# when creating a new container  
RUN apt-get install -y wget  
RUN wget https://s3.amazonaws.com/Minecraft.Download/versions/1.9/1.9.jar -P
~/.minecraft/versions/1.9/  
  
RUN rm -rf /var/www/html/*  
COPY mini.py /overviewer/  
COPY shot.sh /overviewer/  
CMD service nginx start  

