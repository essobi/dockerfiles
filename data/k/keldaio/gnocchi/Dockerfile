# If you get an error message that looks like:  
# Error parsing reference: "keldaio/spark as builder"  
# is not a valid repository/tag: invalid reference format  
# It means that you're running an older version of Docker  
# that doesn't support using "as builder", and you'll  
# need to upgrade.  
FROM keldaio/spark as builder  
  
RUN apt-get update  
RUN apt-get install -y maven scala git  
  
RUN git clone https://github.com/kelda-inc/gnocchi.git -b gnocchiRefactor  
  
# On OSX with the default docker configuration this step fails because it runs  
# out of memory. In Docker -> Preferences -> Advanced you can change the  
# memory limit to 3GB and it should work.  
RUN cd gnocchi && mvn package -DskipTests  
  
FROM keldaio/spark  
COPY \--from=builder ./gnocchi gnocchi/  
  
ENV PATH /gnocchi/bin:$PATH  

