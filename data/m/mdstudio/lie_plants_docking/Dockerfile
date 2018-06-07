FROM mdstudio/mdstudio_docker3:0.0.1  
COPY . /home/mdstudio/lie_plants_docking  
  
RUN chown mdstudio:mdstudio /home/mdstudio/lie_plants_docking  
  
WORKDIR /home/mdstudio/lie_plants_docking  
  
RUN pip install numpy scipy && pip install .  
  
USER mdstudio  
  
CMD ["bash", "entry_point_lie_plants_docking.sh"]  

