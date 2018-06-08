FROM ravellosystems/public-general-slave:latest  
  
#Install python libraries  
RUN apt-get update  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN pip install --upgrade pip  
RUN pip install docker-py  
RUN pip install requests  
RUN pip install futures  
RUN pip install simplejson  
RUN pip install python-dateutil  
RUN pip install fabric  
RUN pip install jprops  
RUN pip install ravello-sdk  
RUN pip install mockito  
RUN pip install nose  
RUN pip install numpy  
RUN apt-get install -y python-numpy python-scipy python-matplotlib ipython
ipython-notebook python-pandas python-sympy python-nose python-sklearn  
  
USER root  
RUN chmod -R 777 /usr/local/lib/python*  
  
# Standard SSH port  
EXPOSE 22  
# Startup services when running the container  
CMD ["/usr/sbin/sshd -D"]  

