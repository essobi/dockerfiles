FROM mauritsd/ibivu_course_base:latest  
MAINTAINER "Maurits Dijkstra" <m.j.j.dijkstra@vu.nl>  
  
RUN echo "deb http://deb.debian.org/debian wheezy main" >> \  
/etc/apt/sources.list && apt-get update  
  
RUN apt-get install -y \  
dssp \  
python \  
python-biopython \  
libglib2.0 \  
python-matplotlib  
  
RUN apt-get install -t wheezy -y gromacs  
  
COPY /packages /packages  
RUN KEY_MODELLER=MODELIRANJE dpkg -i /packages/modeller_9.17-1_amd64.deb; \  
rm -rf /packages/  
  
ADD /workspace_template /workspace_template  

