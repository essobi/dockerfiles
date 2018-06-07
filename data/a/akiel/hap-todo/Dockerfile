FROM java:8  
ENV LEIN_ROOT true  
ADD https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
/usr/local/bin/lein  
RUN chmod +x /usr/local/bin/lein  
  
COPY src /app/src  
COPY project.clj /app/  
  
WORKDIR /app  
  
RUN lein with-profile production deps  
  
EXPOSE 80  
ENV PORT 80  
ENV JVM_OPTS -server -Xmx64m  
  
CMD ["lein", "with-profile", "production", "trampoline", "run"]  

