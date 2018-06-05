# Dockerfile for light-weight data-filter  
FROM openwhisk/dockerskeleton  
  
ENV FLASK_PROXY_PORT 8080  
#Time librari for python  
RUN pip install pytz  
  
### Add source file(s)  
RUN rm /action/exec  
#RUN mkdir /actions/  
ADD exec /action/  
#ADD dewpoint.py /actions/ #dewpoint new  
#ADD par.py /actions/ #par radiation  
#ADD ec.py /actions/ #electroconductivity transformation  
#ADD smcal.py /actions/ #DECAGON SOIL CALIBRATIONS  
#ADD smocal.py /actions/ #AFE SOIL CALIBRATION  
#ADD radcal.py /actions/ #RADIATION JOPIA CALIBRATION  
#ADD timeconv.py /actions/ #time convertion to chilean hour, month day and
minute  
#ADD gdd.py /action/ #growing degree days  
RUN chmod +x /action/exec  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]  

