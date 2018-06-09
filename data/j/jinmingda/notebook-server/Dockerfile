FROM ipython/scipystack  
  
MAINTAINER Mingda Jin  
  
RUN apt-get update && apt-get install -y \  
vim \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y  
  
VOLUME /mnt  
WORKDIR /mnt  
  
EXPOSE 8888  
ADD requirements.txt /  
RUN pip2 install -r /requirements.txt  
RUN pip3 install -r /requirements.txt  
  
ADD notebook.sh /  
RUN chmod +x /notebook.sh  
  
CMD ["/notebook.sh"]  

