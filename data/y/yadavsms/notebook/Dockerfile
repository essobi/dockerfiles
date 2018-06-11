#Purpose: Docker ipython image  
#Author: Somesh Yadav  
#pull ubuntu latest image from docker hub  
FROM ubuntu:latest  
  
MAINTAINER Somesh Yadav<somesh.yadav@imaginea.com>  
  
#update apt repo  
RUN apt-get update  
  
#install ipython  
RUN apt-get install -y ipython ipython-notebook  
  
#Create new profile for ipython  
RUN ipython profile create nbserver  
  
#Add ipython notebook config file  
ADD ipython_notebook_config.py /root/.ipython/profile_nbserver/  
  
#Create /notebook directory for notebooks  
RUN mkdir /notebook/  
  
ADD notebook.sh /  
  
RUN chmod +x /notebook.sh  
  
WORKDIR /notebook/  
  
#expose port 8888  
EXPOSE 8888  
CMD ["/notebook.sh"]  

