# vim: ft=dockerfile  
#  
# @package gulp  
# @author yannoff <https://github.com/yannoff>  
# @license MIT  
#  
FROM node:alpine  
  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
ENV PATH $PATH:/src/node_modules/.bin  
  
RUN ln -s /usr/bin/entrypoint.sh /  
  
ENTRYPOINT "entrypoint.sh"  
WORKDIR "/src"  

