FROM python:3.4  
# Local directory with project source  
ENV DOCKYARD_SRC=ticket_system  
# Directory in container for all project files  
ENV DOCKYARD_SRVHOME=/srv  
# Directory in container for project source files  
ENV DOCKYARD_SRVPROJ=/srv/ticket_system  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create application subdirectories  
WORKDIR $DOCKYARD_SRVHOME  
  
# Copy application source code to SRCDIR  
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ  
  
# Install Python dependencies  
RUN pip3 install -r $DOCKYARD_SRVPROJ/requirements.txt  
  
EXPOSE 8000  
# Copy entrypoint script into the image  
WORKDIR $DOCKYARD_SRVPROJ  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["sh", "./docker-entrypoint.sh"]

