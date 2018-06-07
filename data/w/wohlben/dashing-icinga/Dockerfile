FROM ruby  
ADD dashing-icinga /defaults/dashing-icinga  
RUN apt-get update && apt-get install -y nodejs rsync  
RUN cd /defaults/dashing-icinga/ && bundle  
  
ADD entrypoint.sh /entrypoint.sh  
CMD /entrypoint.sh  
  

