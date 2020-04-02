##################################################
# Dockerfile for
# https://github.com/author_name/project_name
##################################################


############
# Base image
############

FROM continuumio/miniconda3
# It runs on Debian GNU/Linux 8; use e.g. uname -a ; cat /etc/issue.net
# https://hub.docker.com/r/continuumio/miniconda/
# Or simply run:
# docker run --rm -ti continuumio/miniconda3
# docker run --rm -ti ubuntu


#########
# Contact
#########
MAINTAINER author_name <author_email>

#########################
# Update/install packages
#########################

# Install system dependencies
# If running on Debian and anaconda/miniconda image, use apt-get:
RUN apt-get update && apt-get upgrade -qy apt-utils

RUN apt-get install -qy gcc \
    g++ \
    tzdata \
    wget \
    bzip2 \
    unzip \
    sudo \
    bash \
    fixincludes

# Get plotting libraries:
RUN apt-get install -qy \
            inkscape \
            graphviz

#########################
# Install conda
#########################

# Miniconda:
#RUN cd /usr/bin \
#    && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
#    && bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda

#RUN export PATH="/usr/local/miniconda/bin:$PATH"

# Add conda channels, last to be added take priority
# Don't mix conda-forge and/or bioconda with defaults channel in R as packages
# will conflict with other and fail
# channels
RUN conda config --add channels bioconda \
    && conda config --add channels conda-forge \
    && conda config --remove channels defaults \
    && conda config --remove channels r

# Update conda:
RUN conda update -y conda

#########################
# Install dependencies
#########################

##########
# Install all packages needed
# Major packages:
RUN conda install python=3.6 \
    && conda install -y r

# Install python packages:
RUN pip install --upgrade pip numpy setuptools \
    && pip install cython \
    && pip install pandas \
    && pip list

# Install project specific packages:
RUN conda install -y r-docopt=0.4.5 r-data.table=1.10.4 r-ggplot2=2.2.1 ; \
    R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("cowplot", repos = "http://cran.us.r-project.org") ; library("cowplot")' ; \
    R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("ggthemes", repos = "http://cran.us.r-project.org") ; library("ggthemes")' ; \
    R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("rprojroot", repos = "http://cran.us.r-project.org") ; library("rprojroot")'
#R --vanilla -e 'source("https://bioconductor.org/biocLite.R") ; install.packages("bigpca", repos = "http://cran.us.r-project.org") ; library("bigpca")' ; \

# Install rpy2 with conda as pip version causes conflicts:
#RUN conda install -y rpy2
##########

##########
# Install packages that aren't on pip or conda:

# eg FlashPCA2 and dependencies:

# Eigen: http://eigen.tuxfamily.org/index.php?title=Main_Page
# Eigen has a conda recipe though: conda install -c menpo eigen
#RUN cd ; \
#    mkdir flashpca2 ; \
#    wget http://bitbucket.org/eigen/eigen/get/3.3.4.tar.gz ; \
#    tar xvfz 3.3.4.tar.gz \
#    mv eigen-eigen-5a0156e40feb eigen ; \
#    cd eigen ;
##########


##############################
# Install package of interest
##############################

RUN pip install git+git://github.com/EpiCompBio/stats_utils.git

############################
# Default action to start in
############################
# Only one CMD is read (if several only the last one is executed)
#ENTRYPOINT ['/xxx']
#CMD echo "Hello world"
#CMD project_quickstart.py
CMD ["/bin/bash"]

# To build run as:
#docker build --no-cache=true -t antoniojbt/pipe_tests_alpine .

# To run e.g.:
# docker run --rm -ti antoniojbt/pipe_tests

# If mounting a volume do e.g.:
# docker run -v /host/directory:/container/directory --rm -ti antoniojbt/pipe_tests
# docker run -v ~/Documents/github.dir/docker_tests.dir:/home/ --rm -ti antoniojbt/pipe_tests_alpine

# Create a shared folder between docker container and host
#VOLUME ["/shared/data"]
