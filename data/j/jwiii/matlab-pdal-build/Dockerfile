FROM pdal/dependencies  
  
RUN git clone \--depth=1 https://github.com/PDAL/PDAL --branch master
--single-branch \  
&& cd PDAL \  
&& mkdir build  
  
# for convenience  
RUN apt-get update \  
&& apt-get install nano locate \  
&& updatedb  
  
ENV PATH="/matlab/bin:$PATH"  
WORKDIR /PDAL/build  
  
COPY build.sh /PDAL/build  
  
CMD ["/PDAL/build/build.sh"]  

