FROM xblaster/juridic-ai-extraction:v0  
  
ADD config /config  
#RUN cd /app  
RUN pip install -r /config/requirements.txt  
  
RUN rm -rf /app  
ADD ui /app/ui  
ADD assets /app/assets  
ADD webservice.py /app/  
ADD *.prep /app/  
ADD *.raw /app/  
ADD tensor_text.py /app/  
ADD ref /app/ref  
ADD *.hdf5 /app/  
ADD *.txt /app/  
RUN cd /app  
WORKDIR /app  
CMD python webservice.py  

