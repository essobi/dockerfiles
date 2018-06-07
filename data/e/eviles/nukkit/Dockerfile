FROM eviles/alpine-oracle-jdk8  
  
RUN mkdir -p /var/nukkit \  
&& curl -L --url
"http://ci.mengcraft.com:8080/job/Nukkit/lastSuccessfulBuild/artifact/target/nukkit-1.0-SNAPSHOT.jar"
-o /var/nukkit/nukkit.jar \  
&& echo "[program:nukkit]" >> /etc/supervisord.conf \  
&& echo "directory=/var/nukkit" >> /etc/supervisord.conf \  
&& echo "command=java -jar /var/nukkit/nukkit.jar" >> /etc/supervisord.conf \  
&& echo "stdout_logfile=/dev/stdout" >> /etc/supervisord.conf \  
&& echo "stdout_logfile_maxbytes=0" >> /etc/supervisord.conf \  
&& echo "stderr_logfile=/dev/stderr" >> /etc/supervisord.conf \  
&& echo "stderr_logfile_maxbytes=0" >> /etc/supervisord.conf  
#For default setting...  
ADD nukkit.yml /var/nukkit/  
  
EXPOSE 19132  

