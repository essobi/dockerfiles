FROM grahamdumpleton/warp0-debian8-python27  
  
USER 0  
RUN apt-get update && apt-get install -y libfreetype6 libfreetype6-dev \  
libpng++ libpng++-dev liblapack-dev libatlas-dev gfortran && \  
rm -r /var/lib/apt/lists/*  
  
USER 1001  
RUN pip install --no-cache-dir jupyter ipython[notebook] matplotlib \  
sympy ipyparallel scipy  
  
COPY ipython/ /opt/app-root/ipython/  
COPY jupyter/ /opt/app-root/jupyter/  
  
COPY app.sh /opt/app-root/app.sh  
  
ENV WARPDRIVE_SHELL_FILE=/opt/app-root/app.sh  
  
EXPOSE 8080  
EXPOSE 10000-10011  

