# base image
FROM python:3

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#directory to store app source code
RUN mkdir /frontend_code

#switch to /app directory so that everything runs from here
WORKDIR /frontend_code

#copy the app code to image working directory
COPY . /frontend_code

CMD ["python", "-m", "http.server", "1080"]
