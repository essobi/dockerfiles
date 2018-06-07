FROM python:2  
# upgrade image  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# rfcat dependancies  
WORKDIR /tmp  
RUN hg clone https://treemo@bitbucket.org/atlas0fd00m/rfcat  
WORKDIR /tmp/rfcat  
RUN python setup.py install  
WORKDIR /tmp  
RUN pip install pyusb --pre  
RUN pip install numpy  
RUN pip install ipython  
  
# clean / optimise docker size  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/* /var/tmp/*  
  
# running  
RUN mkdir /root/share  
WORKDIR /root/share  
ENTRYPOINT bash  
  

