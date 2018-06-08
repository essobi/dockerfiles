FROM java:8  
RUN useradd --system --shell /usr/sbin/nologin --home-dir /nonexistent ms  
USER ms  
CMD [ -f /ms/config ] && . /ms/config ; java $MS_JAVA_OPTS -jar
"/ms/${MS_JAR_NAME}"  

