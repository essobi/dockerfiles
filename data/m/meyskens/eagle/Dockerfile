FROM meyskens/desktop-base  
  
ENV version=8.3.2  
  
RUN apt-get update && apt-get install -y locales  
  
  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
#RUN wget
http://trial2.autodesk.com/NET17SWDLD/2017/EGLPRM/ESD/Autodesk_EAGLE_${version}_English_Linux_64bit.tar.gz
&& \  
# tar -xzf Autodesk_EAGLE_${version}_English_Linux_64bit.tar.gz && \  
# rm -fr Autodesk_EAGLE_${version}_English_Linux_64bit.tar.gz  
# Sorry need older version  
COPY ./eagle /eagle-${version}  
  
USER user  
  
ENV LIBGL_ALWAYS_SOFTWARE=1  
  
CMD /eagle-${version}/eagle

