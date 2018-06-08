FROM python:2.7  
ADD ./src /sepia  
  
RUN echo 'America/Sao_Paulo' | tee /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& pip install -r /sepia/requirements.txt  
  
VOLUME /sepia/rss  
  
CMD python /sepia/main.py 'http://www.goal.com/br/news/archive/1?ICID=OP'
'div' 'class' 'articleInfo' 'UTF-8' 'div' 'class' 'article-text' 'go.xml'  

