FROM cuckoohello/pytorch  
ENV USER jupyter  
ENV UID 1000  
ENV ROOT_PASSWORD jupyter  
  
RUN apt-get update && apt-get install --no-install-recommends -y gosu openssh-
client && apt-get clean && \  
pip install jupyter  
COPY entrypoint.sh /  
COPY docker-compose.yml /  
VOLUME /workspace  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["notebook", "--ip=0.0.0.0"]  

