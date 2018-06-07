FROM shincoder/homestead  
MAINTAINER Alexandr Shevchenko <alexandr@comet.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf  
ADD ./prepare.sh /prepare.sh  
ADD ./serve.sh /serve.sh  
ADD ./serve_oxwall.sh /serve_oxwall.sh  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /*.sh  
RUN /prepare.sh  
  
EXPOSE 80 22 20 21 35729 9876 465 25  
CMD ["/entrypoint.sh"]

