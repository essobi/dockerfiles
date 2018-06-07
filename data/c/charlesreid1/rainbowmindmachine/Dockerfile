# This container defines a base rainbow mind machine image.  
# This base container image is used to build other twitter bots.  
FROM jfloff/alpine-python:recent-onbuild  
RUN git clone -b tripos-fix https://git.charlesreid1.com/bots/b-rainbow-mind-
machine.git /rmm  
RUN cd /rmm && \  
/usr/bin/env pip install -r requirements.txt && \  
/usr/bin/env python /rmm/setup.py build && \  
/usr/bin/env python /rmm/setup.py install  

