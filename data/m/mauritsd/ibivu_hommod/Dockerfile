FROM mauritsd/ibivu_course_base:latest  
MAINTAINER "Maurits Dijkstra" <m.j.j.dijkstra@vu.nl>  
  
RUN apt-get update && apt-get install -y \  
python \  
python-biopython  
  
COPY /packages /packages  
RUN KEY_MODELLER=MODELIRANJE dpkg -i /packages/modeller_9.17-1_amd64.deb; \  
rm -rf /packages/  
  
ADD /workspace_template /workspace_template  

