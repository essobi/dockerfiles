FROM centos:6  
MAINTAINER Huy Doan <me@huy.im>  
VOLUME /magma  
ENV TERM dumb  
  
COPY magma /build  
COPY scripts /scripts  
RUN chmod -v +x /scripts/*.sh  
  
RUN /scripts/build.sh  
  
EXPOSE 25 465 110 995 143 993 10000 10500  
ENTRYPOINT ["/scripts/entrypoint.sh"]  
CMD ["run"]  

