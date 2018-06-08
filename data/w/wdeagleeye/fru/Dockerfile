FROM wdeagleeye/eaglebase:latest  
  
RUN easy_install web.py  
RUN pip install boto  
RUN pip install queuelib  
RUN pip install pillow  
ADD . /fru  
#RUN ls -ltr /fru  
CMD cd /fru && python2.7 facerecognizer.py

