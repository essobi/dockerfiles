FROM hoshinotsuyoshi/vncserver  
  
RUN mkdir -p /data/web  
ADD Gemfile /data/web/Gemfile  
ADD Gemfile.lock /data/web/Gemfile.lock  
RUN cd /data/web && bundle --jobs 4  
  
# web app  
ADD . /data/web  
  
CMD ["/data/web/start.sh"]  

