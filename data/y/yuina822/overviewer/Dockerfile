FROM python:2.7  
ADD entrypoint.sh /  
ADD config.py /  
  
RUN pip install numpy  
RUN pip install Pillow  
RUN apt-get update  
RUN apt-get install -y python-pil  
RUN ln -s /usr/include/python2.7/Imaging.h /usr/include/Imaging.h  
RUN ln -s /usr/include/python2.7/ImPlatform.h /usr/include/ImPlatform.h  
  
RUN mkdir -p /usr/src/app/overviewer  
WORKDIR /usr/src/app/overviewer  
RUN git clone https://github.com/overviewer/Minecraft-Overviewer.git .  
RUN python ./setup.py build  
  
ENTRYPOINT /entrypoint.sh  

