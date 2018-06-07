FROM fabric8/hubot-base:v1.0.0  
MAINTAINER fabric8.io <fabric8@googlegroups.com>  
  
RUN yo hubot --owner="fabric8.io <fabric8@googlegroups.com>" \--name="fabric8"
\--description="Platform manager" \--adapter=slack --defaults  
  
ADD external-scripts.json /home/hubot/  
  
CMD bin/hubot -a slack  

