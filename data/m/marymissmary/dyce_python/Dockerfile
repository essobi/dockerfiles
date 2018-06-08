##  
## Container for testing DyCE  
##  
FROM marymissmary/dyce  
  
#RUN apt-get update && apt-get install -y python  
RUN apt-get upgrade -y && apt-get update && apt-get install -y \--fix-missing
python  
RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py  
RUN chmod u+x get-pip.py  
RUN python get-pip.py  
RUN rm get-pip.py  
RUN pip install requests  
RUN pip install httpie  
RUN pip install ipython  
  
RUN apt-get install -y python-numpy python-matplotlib  
  
RUN echo 'export PS1="\033[0;34m\u@python-dyce:/# \033[0m"' >> /root/.bashrc  
  

