FROM gentoo/portage:latest as portage  
  
FROM gentoo/stage3-amd64:latest as builder  
COPY \--from=portage /usr/portage /usr/portage  
RUN emerge dev-python/pip  
RUN cd /usr/lib/python3.5/site-packages && patch -p1 -R < /usr/portage/dev-
python/pip/files/pip-disable-system-install.patch  
COPY overlay-packagelist /usr/src/overlay-packagelist/  
COPY setup.py /usr/src/overlay-packagelist/  
RUN cd /usr/src/overlay-packagelist && pip install .  
RUN emerge -c dev-python/pip  
RUN rm -rf /usr/portage  
  
FROM scratch  
COPY \--from=builder / /  
  
ENTRYPOINT ["overlay-packagelist"]  

