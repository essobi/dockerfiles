FROM uweloydl/robot-base:latest  
USER root  
  
#========================  
# python dependencies  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
python \  
python-setuptools \  
python-wheel \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
#==============================  
# robotframework and libraries  
#==============================  
RUN pip install --upgrade pip  
RUN pip install requests==2.9.1  
RUN pip install robotframework==3.0  
RUN pip install robotframework-selenium2library==1.7.4  
RUN pip install robotframework-httplibrary==0.4.2  
RUN pip install robotframework-requests==0.4.5  
RUN pip install robotframework-pabot==0.23  
  
#==============================  
# folder to mount tests  
#==============================  
RUN mkdir -p /opt/robot  
RUN chown -R seluser /opt/robot  
  
#==============================  
# runners  
#==============================  
COPY run-tests.py /opt/robot/bin/run-tests.py  
  
USER seluser  
  
ENTRYPOINT ["/opt/robot/bin/run-tests.py"]  

