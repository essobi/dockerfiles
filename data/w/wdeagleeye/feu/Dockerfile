FROM python:2.7.11  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y --force-yes dist-upgrade  
RUN apt-get install -y --force-yes ffmpeg  
RUN ffmpeg -version  
RUN pip install bottle  
RUN pip install boto3  
RUN pip install requests  
ADD . /feu  
RUN ls -ltr /feu  
CMD cd /feu && python2.7 FrameExtractionUnit.py  
#CMD ["bash"]  

