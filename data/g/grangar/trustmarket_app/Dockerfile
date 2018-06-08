FROM jeanblanchard/java:jdk-8  
EXPOSE 9000  
ENV SM_IMAGE grangar/trustmarket_app  
ENV PATH $PATH:/play-2.2.6  
RUN apk --update add ca-certificates git bash\  
&& apk del git \  
&& cd .. && rm -rf $NGINX \  
&& rm -rf /var/cache/apk/* \  
&& wget http://downloads.typesafe.com/play/2.2.6/play-2.2.6.zip \  
&& unzip play-2.2.6.zip \  
&& rm play-2.2.6.zip \  
&& cd play-2.2.6 \  
&& echo -e "\n2\n" | play new trustmarket  
  
ADD . /play-2.2.6/trustmarket/  
ADD ./pdf /play-2.2.6/repository/cache/pdf  
WORKDIR /play-2.2.6/trustmarket  
RUN play clean compile stage  
  
CMD ["target/universal/stage/bin/trustmarket"]  

