FROM lachele/ambertools:16u15  
  
RUN apt-get update  
RUN apt-get install -y python-dev python-pip  
RUN apt-get install -y openbabel pymol  
  
RUN echo "source /usr/local/amber16/amber.sh" > /root/.bashrc  
  
RUN sed -i "s,python2.7,/usr/bin/python2.7,g" /usr/bin/pymol  
  

