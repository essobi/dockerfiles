FROM centos/python-35-centos7:latest  
  
LABEL io.k8s.description="Wheelhouse (Python 3.5)" \  
io.k8s.display-name="Wheelhouse (Python 3.5)" \  
io.openshift.tags="builder,python,python35,wheelhouse" \  
io.openshift.s2i.scripts-url="image:///opt/app-root/s2i"  
  
COPY assemble /opt/app-root/s2i/  
COPY run /opt/app-root/s2i/  
COPY save-artifacts /opt/app-root/s2i/  
COPY usage /opt/app-root/s2i/  
  
RUN mkdir /opt/app-root/wheelhouse  

