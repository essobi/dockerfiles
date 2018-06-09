FROM apsl/thumbor  
RUN mkdir /usr/local/lib/python2.7/site-packages/blah  
RUN touch /usr/local/lib/python2.7/site-packages/blah/__init__.py  
COPY ./rus_pl8_detector.py /usr/local/lib/python2.7/site-packages/blah/  
COPY ./haarcascade_licence_plate_rus_16stages.xml /usr/src/app/  
ENV DETECTORS="['blah.rus_pl8_detector']"  

