FROM alexarchambault/jupyter-scala-base  
  
MAINTAINER negokaz <negokaz@gmail.com>  
  
ENV SCALA_210_VERSION 2.10.5  
ENV SCALA_211_VERSION 2.11.6  
ENV JUPYTER_SCALA_VERSION 0.2.0-SNAPSHOT  
  
RUN curl -s
https://oss.sonatype.org/content/repositories/snapshots/com/github/alexarchambault/jupyter/jupyter-
scala-cli_${SCALA_210_VERSION}/${JUPYTER_SCALA_VERSION}/jupyter-
scala_${SCALA_210_VERSION}-${JUPYTER_SCALA_VERSION}.tar.xz \  
| tar -Jx -C /opt/ \  
&& /opt/jupyter-
scala_${SCALA_210_VERSION}-${JUPYTER_SCALA_VERSION}/bin/jupyter-scala \  
&& curl -s
https://oss.sonatype.org/content/repositories/snapshots/com/github/alexarchambault/jupyter/jupyter-
scala-cli_${SCALA_211_VERSION}/${JUPYTER_SCALA_VERSION}/jupyter-
scala_${SCALA_211_VERSION}-${JUPYTER_SCALA_VERSION}.tar.xz \  
| tar -Jx -C /opt/ \  
&& /opt/jupyter-
scala_${SCALA_211_VERSION}-${JUPYTER_SCALA_VERSION}/bin/jupyter-scala  
  
ENTRYPOINT ["ipython", "notebook", "--ip=0.0.0.0","--port=8888", "--no-
browser"]  

