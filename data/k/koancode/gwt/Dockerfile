FROM openjdk:8-jdk  
# This is meant to serve as a base for GWT development  
# It has the basis for other JVM development environments as well  
MAINTAINER Ryan Mills <ryan@koancode.com>  
  
# Ensure bash is default  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update -qq && apt-get install -y -qq vim ant pylint  
ENV PATH "./:$PATH"  
# GWT 2.7  
RUN mkdir -p ~/share/java; wget -O - --quiet http://goo.gl/t7FQSn -O
gwt-2.7.zip; unzip gwt-2.7.zip -d ~/share/java  
RUN rm gwt-2.7.zip  
ENV GWT_HOME ~/share/java/gwt-2.7.0  
# SDKMAN  
ENV SDKMAN_DIR /usr/local/sdkman  
RUN curl -s https://get.sdkman.io | bash  
# FIX to SDKMAN (#302 caused regression)  
RUN curl -s https://raw.githubusercontent.com/sdkman/sdkman-
cli/65a8dbf5be383dac967ad3791c9ff13b552b0975/src/main/bash/sdkman-path-
helpers.sh \  
\--output /tmp/sdkman-path-helpers.sh && cp /tmp/sdkman-path-helpers.sh
"$SDKMAN_DIR/src/sdkman-path-helpers.sh"  
RUN chmod 755 "$SDKMAN_DIR/bin/sdkman-init.sh"  
  
# Gradle 2.14  
RUN source ~/.bashrc && sdk install gradle 2.14  
ENV GRADLE_HOME "$SDKMAN_DIR/candidates/gradle/current"  
ENV PATH "$GRADLE_HOME/bin:$PATH"  
CMD ["/bin/bash"]  

