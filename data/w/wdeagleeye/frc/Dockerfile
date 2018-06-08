FROM python:2.7.11  
RUN pip install bottle  
RUN easy_install web.py  
RUN pip install boto  
RUN pip install queuelib  
RUN pip install pillow  
RUN pip install requests  
ADD . /frc  
#RUN ls -ltr /frc  
CMD cd /frc && python2.7 facerecognitioncontroller.py  
#CMD ["bash"]

