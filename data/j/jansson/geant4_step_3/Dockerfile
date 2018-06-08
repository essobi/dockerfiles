FROM jansson/geant4_step_2  
  
WORKDIR /tmp/geant4/build  
  
RUN \  
make G4intercoms && \  
make G4expat && \  
make G4zlib && \  
make G4analysis && \  
make G4materials && \  
make G4graphics_reps && \  
make G4geometry && \  
make G4particles && \  
make G4track && \  
make G4digits_hits  

