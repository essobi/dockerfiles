FROM e96tech/baseimage  
MAINTAINER Alex Salt <alex.salt@e96.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
RUN echo "deb http://repo.percona.com/apt trusty main" >
/etc/apt/sources.list.d/percona.list  
RUN apt-get update && apt-get -y --no-install-recommends --no-install-suggests
install ca-certificates qpress percona-xtradb-cluster-56 bind9-host  
  
# install galera-healthcheck  
ADD https://github.com/sttts/galera-
healthcheck/releases/download/v20150303/galera-healthcheck_linux_amd64
/bin/galera-healthcheck  
RUN test "$(sha256sum /bin/galera-healthcheck | awk '{print $1;}')" =
"86f60d9d82b1f9d2d474368ed7e81a0a361508031a292244847136b0ed2ee770"  
RUN chmod +x /bin/galera-healthcheck  
  
# python  
RUN apt-get install -y python3-setuptools && \  
easy_install3 pip  
  
RUN rm -rf /etc/my.cnf /etc/mysql/my.cnf  
ADD my.cnf /etc/mysql/my.cnf  
RUN chown mysql.mysql /etc/mysql/my.cnf  
  
COPY start /start  
RUN chmod 555 /start  
  
ADD service.json /etc/consul/conf.d/  
  
# election service  
ENV CLUSTER_NAME cluster  
ADD elect /elect  
RUN pip install -r /elect/requirements.txt  
RUN mkdir /etc/service/elect && ln -sv /elect/elect.py /etc/service/elect/run  
  
EXPOSE 3306 4444 4567 4568  
VOLUME ["/var/lib/mysql"]  
  
ENTRYPOINT [ "/sbin/my_init", "/start" ]  

