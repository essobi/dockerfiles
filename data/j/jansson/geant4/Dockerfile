FROM jansson/geant4_step_4 AS last_step  
WORKDIR /tmp/geant4/build  
RUN \  
make G4tracking && \  
make G4event && \  
make G4run && \  
make G4error_propagation && \  
make G4interfaces && \  
make G4parmodels && \  
make G4persistency && \  
make G4physicslists && \  
make G4readout && \  
make G4modeling && \  
make G4vis_management && \  
make G4FR && \  
make G4visHepRep && \  
make G4RayTracer && \  
make G4Tree && \  
make G4VRML && \  
make G4visXXX && \  
make G4gl2ps && \  
make G4GMocren && \  
make G4OpenGL && \  
make && \  
make install && \  
echo ". /usr/local/geant4.${GEANT4_VERSION}/bin/geant4.sh" >>
/etc/profile.d/geant4.sh && \  
echo ". \${G4NEUTRONHPDATA}/../../geant4make/geant4make.sh" >>
/etc/profile.d/geant4.sh  
  
FROM jansson/geant4_base  
COPY --from=last_step /usr/local/geant4.${GEANT4_VERSION}
/usr/local/geant4.${GEANT4_VERSION}  
COPY --from=last_step /etc/profile.d/geant4.sh /etc/profile.d  
WORKDIR /root  

