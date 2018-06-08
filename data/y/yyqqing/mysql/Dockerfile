FROM mysql  
  
ENV TZ=Asia/Shanghai  
RUN mv /etc/localtime /etc/localtime_old && ln -snf /usr/share/zoneinfo/$TZ
/etc/localtime && echo $TZ > /etc/timezone

