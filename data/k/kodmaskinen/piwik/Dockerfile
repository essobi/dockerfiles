FROM tutum/apache-php  
  
ENV PIWIK_VERSION 3.2.0  
RUN rm -rf /app/*  
RUN curl -L -O http://builds.piwik.org/piwik-${PIWIK_VERSION}.tar.gz && \  
tar --strip 1 -xzf piwik-${PIWIK_VERSION}.tar.gz && \  
rm piwik-${PIWIK_VERSION}.tar.gz  
RUN chmod a+w /app/config  
  
EXPOSE 80  
VOLUME /app/config  
CMD ["/run.sh"]  

