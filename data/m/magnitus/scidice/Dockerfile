FROM python:2.7  
RUN pip install numpy scipy  
  
COPY SciDice/ /opt/SciDice/  
COPY setup.py SciDiceScript /opt/  
  
WORKDIR /opt/  
RUN python setup.py install  
  
ENTRYPOINT [""]  
CMD ["SciDiceScript"]

