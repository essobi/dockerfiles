FROM java:8  
ENV LEIN_ROOT true  
ADD https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
/usr/local/bin/lein  
RUN chmod +x /usr/local/bin/lein  
  
COPY resources /app/resources  
COPY src /app/src  
COPY project.clj /app/  
COPY docker/start.sh /app/  
  
WORKDIR /app  
  
RUN lein with-profile production,datomic-free deps  
RUN chmod +x start.sh  
  
EXPOSE 80  
CMD ["./start.sh"]  

