FROM momonga/leiningen  
MAINTAINER supermomonga  
  
RUN mkdir -p /craftbukkit  
  
RUN curl
http://tcpr.ca/files/craftbukkit/craftbukkit-1.7.9-R0.1-20140501.232444-18.jar
-o /craftbukkit/craftbukkit.jar  
  
RUN echo "#!/bin/bash\ncd /craftbukkit/\njava -Xmx1536M -jar craftbukkit.jar
-o true" > /usr/local/bin/craftbukkit  
RUN chmod +x /usr/local/bin/craftbukkit  
  
ENTRYPOINT ["/bin/bash"]  

