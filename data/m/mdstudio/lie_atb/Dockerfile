FROM mdstudio/mdstudio_docker3:0.0.1  
COPY . /home/mdstudio/lie_atb  
  
RUN chown mdstudio:mdstudio /home/mdstudio/lie_atb  
  
WORKDIR /home/mdstudio/lie_atb  
  
RUN pip install .  
  
USER mdstudio  
  
CMD ["bash", "entry_point_lie_atb.sh"]  

