FROM mdstudio/mdstudio_docker2:0.0.1  
COPY . /home/mdstudio/lie_pylie  
  
RUN chown mdstudio:mdstudio /home/mdstudio/lie_pylie  
  
WORKDIR /home/mdstudio/lie_pylie  
  
RUN pip install numpy scipy && pip install .  
  
USER mdstudio  
  
CMD ["bash", "entry_point_lie_pylie.sh"]  

