FROM maxexcloo/java  
  
MAINTAINER Fabrizio Lungo <fab@lungo.co.uk>  
  
EXPOSE 8080  
WORKDIR /opt/  
ENV UPSOURCE_VERSION 2.0.3462  
RUN wget -q
https://download.jetbrains.com/upsource/upsource-${UPSOURCE_VERSION}.zip -O
Upsource.zip  
RUN unzip Upsource.zip  
RUN rm Upsource.zip  
WORKDIR /opt/Upsource  
RUN chmod -R a+rwX .  
RUN mv conf .conf  
VOLUME ["/opt/Upsource/conf", "/opt/Upsource/data", "/opt/Upsource/logs",
"/opt/Upsource/backups"]  
  
ADD entry.sh /opt/Upsource/bin/  
  
ENTRYPOINT ["./bin/entry.sh"]  
CMD ["run"]  

