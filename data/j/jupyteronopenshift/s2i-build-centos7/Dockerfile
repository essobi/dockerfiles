FROM centos/s2i-base-centos7:latest  
  
LABEL io.k8s.description="S2I builder for creating S2I builders (CentOS 7)." \  
io.k8s.display-name="S2I Construction Kit (CentOS 7)" \  
io.openshift.tags="builder"  
  
COPY container-entrypoint /usr/bin  
COPY fix-passwd-entry /usr/bin  
  
COPY assemble /usr/libexec/s2i/assemble  
COPY run /usr/libexec/s2i/run  
COPY save-artifacts /usr/libexec/s2i/save-artifacts  
COPY usage /usr/libexec/s2i/usage  
  
RUN chmod +w /etc/passwd && \  
chown -R 1001:0 /usr/libexec/s2i && \  
fix-permissions /usr/libexec/s2i  
  
EXPOSE 8080  
USER 1001  

