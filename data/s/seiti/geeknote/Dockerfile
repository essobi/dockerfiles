FROM python:2  
RUN git clone git://github.com/VitaliyRodnenko/geeknote.git /opt/geeknote \  
&& cd /opt/geeknote \  
&& python setup.py install  
VOLUME ["/root/.geeknote"]  
ENTRYPOINT ["geeknote"]  

