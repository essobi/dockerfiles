FROM python:2-onbuild  
# RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list  
# RUN sudo apt-get update  
# RUN sudo apt-get install certbot -t jessie-backports  
EXPOSE 5000  
CMD [ "python", "-u", "__main__.py" ]  

