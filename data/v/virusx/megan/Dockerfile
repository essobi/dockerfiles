FROM java:8-jre  
ENV MEGAN_VERSION=6_11_4 PATH="/usr/local/megan/tools:${PATH}"  
RUN wget --progress=dot:mega "http://ab.inf.uni-
tuebingen.de/data/software/megan6/download/MEGAN_Community_unix_${MEGAN_VERSION}.sh"
-O /tmp/megan_installer.sh && \  
echo 'o\n1\n/usr/local/megan\n1,3\ny\n/usr/local/bin\n5\n8000\nn' | sh
/tmp/megan_installer.sh && \  
rm -rf /tmp/*

