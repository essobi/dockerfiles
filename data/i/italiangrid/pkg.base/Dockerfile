FROM fedora:rawhide  
  
ENV BUILD_PLATFORM rawhide  
  
ADD rawhide/setup.sh rawhide/settings.xml /  
RUN chmod +x /setup.sh  
  
RUN /setup.sh  
  
ADD Makefile build.sh setup-stage-area.sh upload-artifacts.sh /home/build/  
  
RUN sh /home/build/setup-stage-area.sh && \  
mkdir /packages && chown -R build:build /packages  
  
WORKDIR /home/build  
  
VOLUME /m2-repository  
VOLUME /packages  
VOLUME /stage-area  
  
USER build  
  
CMD sh build.sh  

