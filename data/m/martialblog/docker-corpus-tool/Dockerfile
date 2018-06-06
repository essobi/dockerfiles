FROM perl:5  
# Install dependencies  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
a2ps \  
r-base-core \  
subversion \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download latest source  
RUN svn co svn://svn.code.sf.net/p/multiword/code/software/UCS/trunk /ucs  
  
# Install Perl dependencies  
# TODO: Install RSPerl  
RUN cpanm Pod::Perldoc && \  
cpanm Term::ReadKey && \  
cpanm Statistics::R  
  
# Add new binaries to PATH  
RUN perl /ucs/System/Install.perl -f  
ENV PATH="/ucs/System/bin/:${PATH}"  
VOLUME /data  
CMD ["bash"]  

