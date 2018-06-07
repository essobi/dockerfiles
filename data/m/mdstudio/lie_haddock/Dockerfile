FROM mdstudio/mdstudio_docker3:0.0.1  
COPY . /home/mdstudio/lie_haddock  
  
RUN chown mdstudio:mdstudio /home/mdstudio/lie_haddock  
  
WORKDIR /home/mdstudio/lie_haddock  
  
RUN pip install https://github.com/MD-
Studio/lie_graph/tarball/master#egg=lie_graph  
  
RUN pip install -e .  
  
USER mdstudio  
  
CMD ["bash", "entry_point_lie_haddock.sh"]  

