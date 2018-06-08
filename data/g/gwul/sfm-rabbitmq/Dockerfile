# 3.7.5-management  
FROM
rabbitmq@sha256:d374d705b3f16e3f0ee34ea14d8599cb4c1f1604ae6deef5fefbaf063d0bb9c6  
MAINTAINER Justin Littman <justinlittman@gwu.edu>  
  
ADD start.sh /usr/local/bin/mq_start.sh  
RUN chmod +x /usr/local/bin/mq_start.sh  
  
ENV RABBITMQ_MNESIA_BASE /sfm-data/rabbitmq  
ENV RABBITMQ_LOG_BASE /sfm-data/rabbitmq  
  
ENTRYPOINT ["/usr/local/bin/mq_start.sh"]

