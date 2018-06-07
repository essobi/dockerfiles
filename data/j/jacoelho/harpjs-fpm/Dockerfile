FROM debian:wheezy  
  
#ENV SITENAME=website  
ENV SITENAME website  
  
ADD build.sh /  
ADD run.sh /  
  
RUN /build.sh  
  
CMD [ "/run.sh" ]  

