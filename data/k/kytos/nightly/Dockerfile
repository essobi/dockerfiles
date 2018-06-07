from kytos/base  
  
ENV KYTOS_NAPPS 'kytos/of_core,kytos/of_lldp'  
RUN python3.6 -m pip install https://github.com/kytos/python-
openflow/archive/master.zip  
RUN python3.6 -m pip install https://github.com/kytos/kytos-
utils/archive/master.zip  
RUN python3.6 -m pip install https://github.com/kytos/kytos/archive/master.zip  
  
EXPOSE 6633  
ADD kytos-welcome.txt /tmp/kytos-welcome.txt  
ADD init.sh /init.sh  
CMD /bin/bash /init.sh  

