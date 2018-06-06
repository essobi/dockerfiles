FROM python:3  
RUN apt-get update  
RUN apt-get install --assume-yes vim  
RUN pip3 install filemagic  
  
RUN git clone https://github.com/labgrid-project/labgrid /opt/labgrid  
RUN cd /opt/labgrid && pip3 install -r crossbar-requirements.txt && python3
setup.py install  
RUN find / -name crossbar -type f  
  
RUN echo '#!/bin/bash' > /opt/entry_script.sh  
RUN echo 'cd /opt/labgrid && /usr/local/bin/crossbar start' >>
/opt/entry_script.sh  
RUN chmod a+x /opt/entry_script.sh  
ENTRYPOINT ["/opt/entry_script.sh"]  
  

