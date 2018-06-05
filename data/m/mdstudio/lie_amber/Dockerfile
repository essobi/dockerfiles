FROM mdstudio/mdstudio_docker3:0.0.1 as amber_base  
  
WORKDIR /home/mdstudio  
  
RUN wget http://ambermd.org/downloads/install_ambertools.sh  
  
RUN bash install_ambertools.sh -v 3 --prefix /home/mdstudio --non-conda  
  
RUN rm -rf /home/mdstudio/ambertools.18.binary.tar.bz2  
  
# used amber compiled in previous step  
FROM mdstudio/mdstudio_docker3:0.0.1  
run apt-get update -y && apt-get install swig gcc gfortran libopenbabel-dev
openbabel -y  
  
COPY \--from=amber_base /home/mdstudio/amber18 /home/mdstudio/amber18  
  
COPY entry_point_lie_amber.sh sett* setup.py /home/mdstudio/lie_amber/  
  
COPY lie_amber /home/mdstudio/lie_amber/lie_amber  
  
COPY scripts /home/mdstudio/lie_amber/scripts  
  
RUN chown mdstudio:mdstudio /home/mdstudio/lie_amber  
  
WORKDIR /home/mdstudio/lie_amber  
  
RUN pip install openbabel .  
  
USER mdstudio  
  
CMD ["bash", "entry_point_lie_amber.sh"]  

