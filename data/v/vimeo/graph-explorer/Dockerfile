FROM google/python  
  
RUN mkdir /var/log/graph-explorer  
RUN mkdir /var/lib/graph-explorer  
  
ONBUILD ADD plugins /opt/graph-explorer/plugins  
ONBUILD ADD config.cfg /opt/graph-explorer/config.cfg  
  
RUN pip install graph-explorer  
  
CMD run_graph_explorer.py /opt/graph-explorer/config.cfg  

