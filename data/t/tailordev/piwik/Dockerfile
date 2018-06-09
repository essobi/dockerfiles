FROM tutum/apache-php  
  
ENV PIWIK_VERSION 3.0.1  
RUN rm -rf /app/*  
RUN curl -L http://builds.piwik.org/piwik-${PIWIK_VERSION}.tar.gz | tar -xz
--strip 1  
RUN chmod a+w /app/config  
  
EXPOSE 80  
VOLUME /app/config  
CMD ["/run.sh"]  

