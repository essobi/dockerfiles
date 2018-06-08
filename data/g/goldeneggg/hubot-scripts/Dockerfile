FROM goldeneggg/hubot  
  
MAINTAINER goldeneggg  
  
# add scripts  
ADD ADD_FILES/root/mybot/scripts/examples.coffee
/root/mybot/scripts/examples.coffee  
ADD ADD_FILES/root/mybot/scripts/examples_cron.coffee
/root/mybot/scripts/examples_cron.coffee  
ADD ADD_FILES/root/mybot/scripts/examples_http.coffee
/root/mybot/scripts/examples_http.coffee  
ADD ADD_FILES/root/mybot/scripts/examples_rss.coffee
/root/mybot/scripts/examples_rss.coffee  
ADD ADD_FILES/root/mybot/scripts/examples_http_listener.coffee
/root/mybot/scripts/examples_http_listener.coffee  
ADD ADD_FILES/root/mybot/scripts/examples_lang.coffee
/root/mybot/scripts/examples_lang.coffee  
  
# install npm library  
WORKDIR /root/mybot  
RUN npm install cron parse-rss cheerio  

