FROM quay.io/ivanvanderbyl/docker-nightmare:latest  
  
ENTRYPOINT ["/entrypoint"]  
EXPOSE 5000  
ADD . /workspace  
RUN rm -rf /workspace/node_modules  
RUN yarn install  
  
CMD ["yarn", "start"]  

