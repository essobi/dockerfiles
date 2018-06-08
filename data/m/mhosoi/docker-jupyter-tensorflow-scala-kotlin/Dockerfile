FROM jupyter/datascience-notebook:bb222f49222e  
RUN conda install pymysql -y && pip install
git+https://github.com/catherinedevlin/ipython-sql.git && conda install
--quiet --yes 'tensorflow=1.1*'  
RUN conda install -y graphviz && pip install graphviz pydot-ng  
RUN pip install psycopg2 folium  
RUN conda install --yes -c conda-forge geopandas  
RUN pip install more-itertools  
  
# Jupyter kernels  
# https://github.com/jupyter/jupyter/wiki/Jupyter-kernels  
  
####################################  
# jupyter-scala  
####################################  
##################  
# Java  
# https://github.com/docker-
library/openjdk/blob/e6e9cf8b21516ba764189916d35be57486203c95/8-jdk/Dockerfile  
##################  
USER root  
  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y ca-certificates-java=20161107~bpo8+1 openjdk-8-jre-
headless openjdk-8-jre openjdk-8-jdk \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
USER $NB_USER  
  
RUN curl -L -o jupyter-scala https://git.io/vzhRi \  
&& chmod +x jupyter-scala \  
&& ./jupyter-scala \  
&& rm -f jupyter-scala  
  
####################################  
# kotlin-jupyter  
####################################  
RUN curl -L -o kotlin-jupyter.zip https://github.com/ligee/kotlin-
jupyter/archive/master.zip \  
&& unzip kotlin-jupyter \  
&& cd kotlin-jupyter-master && ./gradlew install && cd ../  
  

