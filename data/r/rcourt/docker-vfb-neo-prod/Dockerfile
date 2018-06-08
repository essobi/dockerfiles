FROM openjdk:8-jdk  
  
RUN apt-get update --quiet --quiet \  
&& apt-get install --quiet --quiet --no-install-recommends lsof \  
&& apt-get install --quiet --quiet --no-install-recommends git maven gzip
python-psycopg2 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH=$PATH:/opt/Brain/target/  
ENV PATH=$PATH:/opt/Brain/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Core/target/classes/  
ENV PATH=$PATH:/opt/owltools/Golr-Client/target/classes/  
ENV PATH=$PATH:/opt/owltools/Lego/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Annotation/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Core/target/classes//target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-NCBI/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Oort/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Parent/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Runner/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Sim/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Solr/target/classes/  
ENV PATH=$PATH:/opt/owltools/OWLTools-Web/target/classes/  
  
RUN export workspace=/opt && cd "${WORKSPACE}" && \  
echo '** Git checkout Brain **' && \  
git clone https://github.com/hdietze/Brain.git && \  
echo '** Git checkout OLS_configs **' && \  
git clone https://github.com/VirtualFlyBrain/OLS_configs.git && \  
echo '** Git checkout VFB_neo4j **' && \  
git clone https://github.com/VirtualFlyBrain/VFB_neo4j.git && \  
echo '** Git checkout VFB_owl **' && \  
git clone https://github.com/VirtualFlyBrain/VFB_owl.git && \  
echo '** Git checkout owltools **' && \  
git clone https://github.com/owlcollab/owltools.git && \  
cd VFB_owl && \  
find . -name '*.gz' -exec gzip -dvf '{}' \; && \  
cd "${WORKSPACE}/Brain/" && \  
mvn -Dgpg.passphrase=default99 -DskipTests=true -Dmaven.javadoc.skip=true
-Dsource.skip=true clean package && \  
cd "${WORKSPACE}" && \  
cd "${WORKSPACE}/owltools/OWLTools-Parent" && \  
mvn -Dgpg.passphrase=default99 -DskipTests=true -Dmaven.javadoc.skip=true
-Dsource.skip=true clean package  
  
RUN export workspace=/opt && \  
cd "${WORKSPACE}/VFB_owl/" && \  
find /opt/ -name '*SNAPSHOT*.jar' -exec cp {} ./lib/ \; && \  
mvn -Dgpg.passphrase=default99 -DskipTests=true -Dmaven.javadoc.skip=true
-Dsource.skip=true clean package  
  
VOLUME /data  
  
RUN mkdir -p $HOME/.neo4j/ && \  
ls -s /data $HOME/.neo4j/data  
  
RUN echo '** Build OLS **' && \  
export workspace=/opt && cd "${WORKSPACE}" && \  
git clone https://github.com/EBISPOT/OLS.git && \  
cp OLS_configs/*.properties OLS/ols-apps/ols-neo4j-app/src/main/resources/ &&
\  
cd OLS && \  
mvn clean package  
  
RUN export workspace=/opt && \  
echo '** loading vfb to OLS **' && \  
java -Xmx2g -jar -Dspring.profiles.active=vfb -Dols.home=${WORKSPACE} ols-
apps/ols-neo4j-app/target/ols-neo4j-app.jar  
  
ENTRYPOINT ["java -Xmx2g -jar -Dspring.profiles.active=vfb -Dols.home=/opt
/opt/ols-apps/ols-neo4j-app/target/ols-neo4j-app.jar"]  
  
  

