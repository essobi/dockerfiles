FROM openjdk:8  
ENV APP_HOME /var/app  
RUN mkdir -p $APP_HOME  
  
WORKDIR $APP_HOME  
  
ENV DATA_FILE data-for-1.2.11.zip  
  
RUN wget http://hanlp.b0.upaiyun.com/$DATA_FILE \  
&& unzip $DATA_FILE \  
&& rm -f $DATA_FILE  

