FROM cadair/python3  
  
RUN pacman -S --noconfirm python-babel python-snowballstemmer python-sphinx-
alabaster-theme python-sphinx_rtd_theme python-sphinx python-feedparser
python-pytz python-lxml python-pyenchant python-pygeoip sqlite git ipython  
RUN pip install willie  
  
RUN useradd willie -m -d /willie  
RUN chown -R willie /willie  
  
USER willie  
  
#CMD ls /  
CMD willie -c /willie/default.cfg  

