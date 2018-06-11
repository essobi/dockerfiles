FROM gliderlabs/alpine:edge  
MAINTAINER William McGann <contact@WilliamMcGann.com>  
  
ENV SLACK_TOKEN=yourtoken RELAY_PASS=supersecret  
EXPOSE 9001  
RUN apk-install weechat py-pip curl  
RUN pip install websocket-client  
  
COPY root /  
  
ADD https://raw.githubusercontent.com/rawdigits/wee-slack/master/wee_slack.py
/root/.weechat/python/autoload/wee_slack.py  
  
CMD ["start-relay"]  

