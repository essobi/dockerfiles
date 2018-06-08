# Build a CentOS based system  
FROM mayoqin/grunt  
LABEL maintainer "Daniel Blezek blezek.daniel@mayo.edu"  
# Install Slicer 4.x  
RUN mkdir -p /grunt  
RUN curl http://slicer.kitware.com/midas3/download?bitstream=561384 | tar xz
-C /grunt  
WORKDIR /  
COPY slicer.gruntfile.yml /grunt.d/gruntfile.yml  
# Configure Slicer environment  
ENV LD_LIBRARY_PATH=/grunt/Slicer-4.6.2-linux-
amd64/lib/Slicer-4.6/:/grunt/Slicer-4.6.2-linux-amd64/lib/Slicer-4.6/cli-
modules:/grunt/Slicer-4.6.2-linux-
amd64/lib/Teem-1.12.0/:grunt/Slicer-4.6.2-linux-amd64/lib/Python/lib  
ENV PATH=/grunt/Slicer-4.6.2-linux-amd64/lib/Slicer-4.6/cli-modules:${PATH}  
# What do we run on startup?  
CMD ["/bin/grunt", "/grunt.d/gruntfile.yml"]  
# We expose port 9901 by default  
EXPOSE 9901:9901  

