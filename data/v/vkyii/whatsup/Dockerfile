FROM vkyii/anaconda:latest  
  
RUN pip install --upgrade pip \  
&& pip install tushare \  
&& pip install Flask \  
&& pip install sqlalchemy \  
&& pip install pymysql \  
&& pip install apscheduler  
  
ENTRYPOINT ["/tini", "--"]  
  
CMD [ "/bin/bash" ]

