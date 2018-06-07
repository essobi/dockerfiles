FROM insighttoolkit/itk-base  
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>  
  
RUN mkdir /home/itk/bin/ITK  
VOLUME ["/home/itk/bin/ITK"]  
RUN mkdir /home/itk/src/ITKDashboard  
RUN mkdir /home/itk/bin/ITKDashboard  
WORKDIR /home/itk/src/ITKDashboard  
RUN git init  
RUN git remote add -t dashboard origin http://itk.org/ITK.git  
RUN git pull origin  
COPY dashboard.cmake /home/itk/src/ITKDashboard/dashboard.cmake  
ADD cmd.sh /tmp/cmd.sh  
CMD /tmp/cmd.sh  

