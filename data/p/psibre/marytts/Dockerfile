FROM maven  
RUN wget https://github.com/marytts/marytts/archive/v5.2.zip && \  
unzip v5.2.zip && \  
rm -f v5.2.zip && \  
mv marytts-5.2 marytts  
RUN cd marytts && \  
mvn install  
CMD /marytts/target/marytts-5.2/bin/marytts-server  
EXPOSE 59125  

