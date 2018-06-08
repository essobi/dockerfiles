FROM jpetazzo/dind  
  
ENV HOME /root  
ADD .docker /root/.docker  
ADD http://j.mp/docker-functions /tmp/  
RUN echo '[ -f /root/.docker ] && source /root/.docker' >> /root/.bashrc  
  
#CMD  

