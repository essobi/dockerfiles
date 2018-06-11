# utopia_fe/Dockerfile  
FROM zulianp/utopia-fe-env:latest  
  
ENV PETSC_DIR /opt/petsc  
ENV MPI_DIR /opt/petsc  
ENV LIBMESH_DIR /libmesh  
ENV LDFLAGS -L/opt/petsc/lib  
ENV CPATH opt/petsc/include:/opt/slepc/include  
ENV LDFLAGS -L/opt/petsc/lib  
  
RUN ls $MPI_DIR/bin | grep mpi  
  
RUN apk add --no-cache curl build-base clang cmake git gfortran linux-headers
m4 perl lapack-dev valgrind-dev gdb  
  
RUN git clone https://zulianp@bitbucket.org/zulianp/utopia.git utopia_cloned  
RUN cd /utopia_cloned && git checkout development && git pull  
  
# compile utopia  
RUN cd /utopia_cloned/utopia && mkdir bin  
RUN cd /utopia_cloned/utopia/bin && \  
cmake .. -DCMAKE_INSTALL_PREFIX=/utopia -DCMAKE_BUILD_TYPE=Release  
  
RUN cd /utopia_cloned/utopia/bin && make -j4  
RUN cd /utopia_cloned/utopia/bin && make install  
  
ENV LD_LIBRARY_PATH /opt/petsc/lib  
RUN cd /utopia_cloned/utopia/bin && ./utopia_exec -verbose && ./utopia_exec
-test none -bench  
  
# compile moonolith  
RUN git clone https://zulianp@bitbucket.org/zulianp/par_moonolith.git
moonolith_cloned  
RUN cd /moonolith_cloned && mkdir bin  
RUN cd /moonolith_cloned/bin && \  
cmake .. -DCMAKE_INSTALL_PREFIX=/par_moonolith -DCMAKE_BUILD_TYPE=Release \  
-DMPI_CXX_COMPILER=$MPI_DIR/bin/mpic++ -DMPI_C_COMPILER=$MPI_DIR/bin/mpicc -DMPI_FOUND=TRUE  
  
RUN cd /moonolith_cloned/bin && make -j4 && make install  
  
# compile utopia_fe  
RUN cd /utopia_cloned/utopia_fe && mkdir bin  
RUN cd /utopia_cloned/utopia_fe/bin && \  
cmake .. -DCMAKE_INSTALL_PREFIX=/utopia_fe -DUTOPIA_DIR=/utopia
-DCMAKE_BUILD_TYPE=Release -DMOONOLITH_DIR=/par_moonolith  
  
RUN cd /utopia_cloned/utopia_fe/bin && make -j4  
RUN cd /utopia_cloned/utopia_fe/bin && make install  
RUN cd /utopia_cloned/utopia_fe/bin && ./utopia_fe_exec -r smg  
  
ENV UTOPIA_DIR /utopia_fe  
ENV LD_LIBRARY_PATH=/opt/petsc/lib/:/libmesh/lib/:/opt/slepc/lib  
  
RUN echo 'export LD_LIBRARY_PATH='$LD_LIBRARY_PATH > setup.sh  
RUN cat setup.sh  
  
CMD ["/bin/sh"]  

