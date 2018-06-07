FROM ubuntu:xenial  
  
ENV username habushu  
ENV uid 1000  
WORKDIR /home/habushu  
  
USER root  
  
RUN useradd -d "/home/$username" -u $uid -m -s /bin/bash $username  
  
RUN apt-get update && apt-get install -y git python virtualenv  
RUN git clone https://github.com/flurischt/habushu.git  
RUN /bin/bash -c "cd habushu && virtualenv venv && source venv/bin/activate &&
pip install -r requirements.txt"  
ADD conf/habushu.cfg /home/habushu/habushu/  
  
EXPOSE 5000  
USER $username  
CMD /home/habushu/habushu/venv/bin/gunicorn -w 2 -b 0.0.0.0:5000 --chdir
/home/habushu/habushu habushu:app --preload  

