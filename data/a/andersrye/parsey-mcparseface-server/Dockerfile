FROM andersrye/syntaxnet-forever  
  
RUN pip install flask  
  
#RUN git clone https://github.com/JoshData/parsey-mcparseface-server.git
/opt/parsefaceserver  
ADD * /opt/parsefaceserver/  
  
WORKDIR /opt/tensorflow  
  
CMD python /opt/parsefaceserver/server.py  

