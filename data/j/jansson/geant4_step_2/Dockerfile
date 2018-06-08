FROM jansson/geant4_step_1  
  
WORKDIR /tmp/geant4/build  
  
RUN \  
make G4ENSDFSTATE && \  
make G4NDL && \  
make PhotonEvaporation && \  
make RadioactiveDecay && \  
make G4ABLA && \  
make G4NEUTRONXS && \  
make RealSurface && \  
make G4EMLOW && \  
make G4PII && \  
make G4SAIDDATA && \  
make G4clhep && \  
make G4global  

