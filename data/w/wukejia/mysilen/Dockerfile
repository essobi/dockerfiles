  
from ubuntu  
  
maintainer j.w.kejia  
  
label description="this docker image is used to make a basic (non-gpu) machine
learning environment."  
  
label version="0.1.1"  
run apt update -y && apt install -y aptitude && \  
aptitude update -y && aptitude upgrade -y && \  
aptitude install -y emacs less && \  
aptitude install -y octave && \  
aptitude install -y python3 python3-pip && \  
pip3 install --upgrade pip && \  
pip3 install jupyter keras matplotlib pandas sklearn tensorflow  

