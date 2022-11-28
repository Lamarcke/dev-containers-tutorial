# Download and install the following image, 
# and use it as base for the container and folowwing commands
FROM mcr.microsoft.com/devcontainers/python:3.10

# Updates pre-installed packges.
RUN sudo apt-get update && sudo apt-get -y --no-install-recommends upgrade 

# Adds the NodeJS repository to a Debian or Ubuntu system.
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

# Installs NodeJS as sudo, using apt.
RUN sudo apt-get install -y nodejs
