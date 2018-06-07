FROM hoshinotsuyoshi/vncserver  
  
RUN apt-get update && apt-get -y install libmagickwand-dev  
RUN mkdir -p /data/crawler  
ADD Gemfile /data/crawler/Gemfile  
ADD Gemfile.lock /data/crawler/Gemfile.lock  
WORKDIR /data/crawler  
RUN bundle -j4  
  
RUN mkdir -p /data/web/public  
  
ADD passwd /root/.vnc/passwd  
# 600にしないとパスワード対話式入力になる、git上で600にしてもだめ  
RUN chmod 0600 /root/.vnc/passwd  
  
ADD . /data/crawler  
CMD ["/data/crawler/start.sh"]  

