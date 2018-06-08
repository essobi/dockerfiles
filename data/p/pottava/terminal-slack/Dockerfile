# Terminal Slack  
#  
# @see https://github.com/evanyeung/terminal-slack  
# export SLACK_TOKEN=?  
# docker run --rm -it -e SLACK_TOKEN pottava/terminal-slack  
FROM pottava/nodejs:6.3  
WORKDIR /app  
  
RUN apk --no-cache add --virtual build-dependencies git \  
&& git clone https://github.com/evanyeung/terminal-slack.git /app \  
&& apk del build-dependencies  
  
ENTRYPOINT ["node"]  
CMD ["main.js"]  

