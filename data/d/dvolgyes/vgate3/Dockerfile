#  
# Dockerfile for GATE 7.0  
# http://www.opengatecollaboration.org/  
#  
# The image is based on the vGate 3.0 image, but it has been modified a bit,
see below.  
#  
#  
#  
  
FROM dvolgyes/vgate3_vanilia  
MAINTAINER David Völgyes <david.volgyes@ ieee org>  
  
# Setting environment variables  
ENV TERM linux  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg-divert --local --rename /usr/bin/ischroot && ln -sf /bin/true
/usr/bin/ischroot  
  
RUN apt-get update  
RUN apt-get install -y --force-yes dialog debconf-utils  
RUN apt-get clean  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DYLD_LIBRARY_PATH /home/gate/Progs/root/lib  
ENV G4LEDATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/G4EMLOW6.32  
ENV G4LEVELGAMMADATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/PhotonEvaporation2.3  
ENV G4NEUTRONHPDATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/G4NDL4.2  
ENV G4NEUTRONXSDATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/G4NEUTRONXS1.2  
ENV G4PIIDATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/G4PII1.3  
ENV G4RADIOACTIVEDATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/RadioactiveDecay3.6  
ENV G4REALSURFACEDATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/RealSurface1.0  
ENV G4SAIDXSDATA
/home/gate/Progs/Geant4/geant4.9.6.p03-install/share/Geant4-9.6.3/data/G4SAIDDATA1.1  
ENV GATEENV /home/gate/Progs/Gate  
ENV LD_LIBRARY_PATH
/home/gate/Progs/Geant4/geant4.9.6.p03-install/lib:/home/gate/Progs/root/lib  
ENV LIBPATH /home/gate/Progs/root/lib  
ENV PATH
/home/gate/Progs/Geant4/geant4.9.6.p03-install/bin:/home/gate/Progs/root/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/gate/Documents/gate_doc/ascii/prog/:/home/gate/Progs/Gate/gate_v7.0-install/bin  
ENV PYTHONPATH /home/gate/Progs/root/lib  
ENV ROOTSYS /home/gate/Progs/root  
ENV SHLIB_PATH /home/gate/Progs/root/lib  
  
ADD profile /etc/profile  
ADD sudoers /etc/sudoers  
ADD bashrc /home/gate/.bashrc  
ADD bash_gate /home/gate/.bash_gate  
RUN rm /home/gate/.bash_history  
RUN chmod 0440 /etc/sudoers  
  
CMD ["su","-l","gate"]  

