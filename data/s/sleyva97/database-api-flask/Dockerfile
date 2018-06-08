FROM mere/base  
  
RUN pacman -Syy python --noconfirm  
  
WORKDIR /tmp/wdir  
  
ADD maintenance_api/ ./maintenance_api  
  
ADD requirements.txt .  
  
ADD setup.py .  
  
RUN pip install . && cd / && rm -rf /tmp/wdir  
  
ENTRYPOINT mapi  

